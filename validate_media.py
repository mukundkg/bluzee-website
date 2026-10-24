"""Validate local media wiring without requesting the remote media objects."""
import csv
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).parent
CONFIG = json.loads((ROOT/'content-source/r2-media.json').read_text())
BASE = CONFIG['media_base_url']
with (ROOT/'content-source/Bluzee_Media_List.csv').open(encoding='utf-8-sig',newline='') as f:
    inventory = {('Videos/' if r['Extension'].lower()=='.mp4' else 'Images/')+r['Name'] for r in csv.DictReader(f)}

class MediaParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.elements=[]
    def handle_starttag(self, tag, attrs):
        self.elements.append((tag,dict(attrs)))

pages={}
used=set()
video_urls=set()
issues=[]
for page in sorted((ROOT/'dist').rglob('*.html')):
    if page.name=='review-mobile.html': continue
    parsed=MediaParser(); parsed.feed(page.read_text())
    name=str(page.relative_to(ROOT/'dist')); pages[name]=parsed
    for tag,attrs in parsed.elements:
        if 'data-video' in attrs:
            video_urls.add(attrs['data-video'])
            for key in ('data-title','data-source'):
                if not attrs.get(key): issues.append(f'{name}: player missing {key}')
        for key,value in attrs.items():
            if value and value.startswith(BASE+'/'):
                object_key=unquote(urlsplit(value).path.lstrip('/'))
                used.add(object_key)
                if object_key not in inventory: issues.append(f'{name}: unknown media key {object_key}')
                if ' ' in value or any(ord(c)>127 for c in value): issues.append(f'{name}: URL not encoded')
        if tag=='img' and 'wixstatic.com' in attrs.get('src',''):
            issues.append(f'{name}: image render still depends on Wix')
        if tag=='a' and 'static.wixstatic.com' in attrs.get('href',''):
            issues.append(f'{name}: full-size photograph still depends on Wix')

configured=set(CONFIG['videos'].values())
configured.update(CONFIG['portraits'].values())
configured.update(CONFIG['logos'].values())
configured.add(CONFIG['appreciation'])
configured.update(x['r2_key'] for x in CONFIG['gallery'].values() if x['r2_key'])
for values in CONFIG['extra_gallery_photos'].values(): configured.update(values)
for key in configured-used: issues.append(f'Configured but absent from built site: {key}')
for key in configured-inventory: issues.append(f'Configured but absent from supplied inventory: {key}')
from r2_media import media_url
for key in CONFIG['videos'].values():
    if media_url(key) not in video_urls: issues.append(f'No player for {key}')
testimonials=[a for t,a in pages['testimonials/index.html'].elements if 'data-video' in a]
if len(testimonials)!=5: issues.append('Expected five testimonial player controls')
launch='https://video.wixstatic.com/video/0ae95f_e907a793ae53467b9dacb8c9428e076d/720p/mp4/file.mp4'
legacy={v for v in video_urls if 'wixstatic.com' in v}
if legacy!={launch}: issues.append(f'Unexpected legacy video dependencies: {legacy}')
if len(pages)!=20: issues.append('Expected 20 built HTML pages')
print(json.dumps({'pages':len(pages),'inventory_files':len(inventory),'mapped_objects':len(used),'mapped_videos':len(CONFIG['videos']),'testimonials':len(testimonials),'remaining_legacy_video_count':len(legacy),'issues':issues},indent=2))
assert not issues

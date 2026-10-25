"""Check unique editorial artwork, responsive assets, and valid page nesting."""
from html.parser import HTMLParser
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlsplit, unquote
import hashlib, json

ROOT=Path(__file__).parent/'dist'
EDITORIAL={'v8-scene','v9-hero-scene','v9-ai-image','v9-guide-landscape','v10-card-media','split-panel'}
VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
uses=defaultdict(list); issues=[]; responsive=0

class Scan(HTMLParser):
    def __init__(self,page):
        super().__init__();self.page=page;self.stack=[];self.hero_count=0
    def handle_starttag(self,tag,attrs):
        global responsive
        a=dict(attrs);classes=set(a.get('class','').split())
        if tag=='source' and 'srcset' in a:
            for ref in a['srcset'].split(','):
                ref=ref.strip().split()[0];u=urlsplit(ref)
                if not u.scheme and not (self.page.parent/unquote(u.path)).exists():issues.append(['missing responsive asset',str(self.page),ref])
                responsive+=1
        if tag=='img' and any(c&EDITORIAL for _,c in self.stack):
            src=a.get('src','');u=urlsplit(src)
            if u.scheme:issues.append(['remote editorial image',str(self.page),src])
            else:
                p=(self.page.parent/unquote(u.path)).resolve()
                if p.exists():uses[str(p.relative_to(ROOT.resolve()))].append(str(self.page.relative_to(ROOT)))
                else:issues.append(['missing artwork',src])
        if tag not in VOID:self.stack.append((tag,classes))
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if tag not in VOID:self.handle_endtag(tag)
    def handle_endtag(self,tag):
        if tag in VOID:return
        if self.stack and self.stack[-1][0]==tag:self.stack.pop()
        else:
            issues.append(['nesting',str(self.page.relative_to(ROOT)),tag,self.stack[-1][0] if self.stack else 'empty'])
            for i in range(len(self.stack)-1,-1,-1):
                if self.stack[i][0]==tag:self.stack=self.stack[:i];break

pages=sorted(ROOT.rglob('index.html'))
for page in pages:
    scan=Scan(page);scan.feed(page.read_text())
for asset,locations in uses.items():
    if len(locations)!=1:issues.append(['repeated editorial artwork',asset,locations])
hashes=defaultdict(list)
for asset in uses:hashes[hashlib.sha256((ROOT/asset).read_bytes()).hexdigest()].append(asset)
for paths in hashes.values():
    if len(paths)>1:issues.append(['same image bytes under different filenames',paths])
for folder in ('products','services'):
    for page in (ROOT/folder).glob('*/index.html'):
        if 'data-v10-offering=' not in page.read_text():issues.append(['missing distinct hero',str(page)])
report={'pages':len(pages),'unique_editorial_images':len(uses),'responsive_sources':responsive,
        'scope':'Decorative backgrounds, portfolio cards, AI stream imagery; original proof thumbnails, document previews and brand marks retain their source identities.',
        'image_usage':dict(sorted(uses.items())),'issues':issues}
(ROOT.parent/'content-source/distinct-v10-image-usage.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['image_usage','scope']},indent=2))
assert not issues

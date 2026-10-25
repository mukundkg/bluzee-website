from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).parent;DIST=ROOT/'dist'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.data=[];self.links=[];self.ids=set();self.meta={};self.canon=[];self.src=[]
 def handle_data(self,data):self.data.append(data)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='meta':self.meta[a.get('name','')]=a.get('content','')
  if tag=='link' and a.get('rel')=='canonical':self.canon.append(a['href'])
  if tag in ['img','source','video','script']:self.src.append(a.get('src',''))
def parse(text):
 p=Parser();p.feed(text);return p
norm=lambda x:re.sub(r'\s+','',x.replace('™',''))
data=json.loads((ROOT/'content-source/legacy-content.json').read_text());issues=[]
for post in data['posts']:
 original=norm(''.join(parse(post['body_html']).data))
 page=parse((DIST/'post'/post['slug']/'index.html').read_text())
 if original not in norm(''.join(page.data)):issues.append('Article text changed: '+post['slug'])
 if post['author'] not in ''.join(page.data):issues.append('Author missing: '+post['slug'])
 for src in page.src:
  if 'wixstatic' in src:issues.append('Wix image: '+src)
pages=list(DIST.rglob('*.html'))
for path in pages:
 name=path.relative_to(DIST).as_posix();p=parse(path.read_text())
 if name=='design-notes/index.html':continue
 if len(p.canon)!=1 or not p.canon[0].startswith('https://www.bluzee.xyz/'):issues.append('Canonical: '+name)
 if name!='404.html' and p.meta.get('robots')!='index,follow':issues.append('Indexing: '+name)
 for href in p.links:
  if urlsplit(href).netloc in ['www.bluzee.xyz','bluzee.xyz']:issues.append('Unmigrated own-domain link: '+name+' '+href)
 if 'Concept notes' in ''.join(p.data):issues.append('Concept footer: '+name)
aliases=json.loads((ROOT/'content-source/launch-pages.json').read_text())['aliases']
for source,target in aliases.items():
 t=urlsplit(target);dest=DIST/t.path.lstrip('/')
 if dest.is_dir():dest=dest/'index.html'
 if not dest.exists():issues.append('Redirect target missing: '+target)
 elif t.fragment and t.fragment not in parse(dest.read_text()).ids:issues.append('Redirect anchor missing: '+target)
sitemap=ET.parse(DIST/'sitemap.xml')
locs=[x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
if len(locs)!=41 or len(locs)!=len(set(locs)):issues.append('Sitemap count/duplicates')
headers=(DIST/'_headers').read_text()
assert 'https://:project.pages.dev/*' in headers and 'https://:version.:project.pages.dev/*' in headers
assert (DIST/'404.html').exists()
assert not list(DIST.glob('_qa*'))
print(json.dumps({'pages':len(pages),'articles_preserved':len(data['posts']),'sitemap_entries':len(locs),'legacy_images':len(data['assets']),'issues':issues},indent=2))
assert not issues

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json, re
root=Path(__file__).parent/'dist'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=[];self.h1=0;self.data=[];self.links=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs)
  if t=='h1':self.h1+=1
  if 'id' in d:self.ids.append(d['id'])
  if t in ['a','link','img','script']:
   v=d.get('href') or d.get('src')
   if v:self.refs.append(v)
  if t=='a':self.links.append(d)
 def handle_data(self,d):self.data.append(d)
issues=[];pages=sorted(p for p in root.rglob('*.html') if p.name!='review-mobile.html')
for page in pages:
 p=Parser();p.feed(page.read_text())
 if p.h1!=1:issues.append([str(page),'h1',p.h1])
 if len(p.ids)!=len(set(p.ids)):issues.append([str(page),'duplicate IDs'])
 for ref in p.refs:
  x=urlsplit(ref)
  if x.scheme or x.netloc:continue
  path=((root/unquote(x.path).lstrip('/')) if x.path.startswith('/') else (page.parent/unquote(x.path))).resolve() if x.path else page
  if not path.exists():issues.append([str(page),'missing',ref])
  elif x.fragment and path.suffix=='.html':
   target=Parser();target.feed(path.read_text())
   if x.fragment not in target.ids:issues.append([str(page),'missing anchor',ref])
 if 'Pilora' in ' '.join(p.data):issues.append([str(page),'obsolete product name'])
 print(page.relative_to(root),'links',len(p.links))
print('PAGES',len(pages),'ISSUES',json.dumps(issues))
assert not issues

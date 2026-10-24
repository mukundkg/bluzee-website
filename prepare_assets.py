from pathlib import Path
from PIL import Image
import shutil,re,urllib.request,concurrent.futures,fitz,json
ROOT=Path('/workspace/scratch/a23a2b861946');OUT=ROOT/'bluzee-web-concept/dist';A=OUT/'assets'
assets={'hero-sculpture':'generated_images/exec-37b974c0-a55e-4679-ad24-e060ca760b78.png','consulting':'assets/service_brochures/consulting.png','implementation':'assets/service_brochures/implementation.png','talent':'assets/service_brochures/talent.png','erp-hub':'assets/service_brochures/erp_hub.png','ai-hub':'assets/ai_streams/cover.png','dypc':'assets/service_brochures/dypc.png','support':'assets/erp_support/cover.png','ai-application':'assets/ai_streams/ai_application.png','full-stack':'assets/ai_streams/full_stack.png','dimaq':'assets/hero.png','network':'assets/network.png'}
for name,src in assets.items():
 im=Image.open(ROOT/src).convert('RGB');im.thumbnail((1600,1600));im.save(A/f'{name}.webp',quality=86,method=6)
for name,src in [('bluzee-logo.png','bluzee_logo.png'),('odoo-learning-partner.png','odoo_learning_partner_source.png')]:shutil.copy2(ROOT/'assets/service_brochures'/src,A/name)
for f in (ROOT/'website-research/brochures').glob('*.pdf'):shutil.copy2(f,OUT/'brochures'/f.name)
css=(ROOT/'website-research/google-fonts.css').read_text();blocks=re.findall(r'@font-face\s*\{.*?\}',css,re.S)
selected=[]
for block in blocks:
 fam=re.search(r"font-family:\s*'([^']+)'",block).group(1);weight=re.search(r'font-weight:\s*(\d+)',block).group(1)
 if weight not in ('400','600','700'):continue
 url=re.search(r'url\(([^)]+)\)',block).group(1);fn=fam.lower().replace(' ','-')+'-'+weight+'.ttf'
 selected.append((url,fn,block))
def fetch(item):
 url,fn,block=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  data=urllib.request.urlopen(req,timeout=40).read();(A/fn).write_bytes(data)
  return block.replace(url,fn)
 except Exception as e:print('Font fallback',fn,type(e).__name__);return ''
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:local_css=list(ex.map(fetch,selected))
(A/'fonts.css').write_text('\n'.join(local_css))
(A/'font-attribution.txt').write_text('Space Grotesk and Manrope from Google Fonts. SIL Open Font License. Sources: https://fonts.google.com/specimen/Space+Grotesk and https://fonts.google.com/specimen/Manrope.\n')
d=fitz.open(OUT/'brochures/Bluzee_Dimaq_Brochure.pdf');assert len(d)==13
assert all(len(p.get_text().strip())>20 for p in d)
print(json.dumps({'images':len(assets),'brochures':len(list((OUT/'brochures').glob('*.pdf'))),'dimaq_pages':len(d),'fonts':len(list(A.glob('*.ttf')))}))

import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
photos=[]
for path in (root/'content/photos').glob('*.json'):
    p=json.loads(path.read_text(encoding='utf-8'))
    if p.get('image') and p.get('category'):  
        photos.append({'title':p.get('title','Untitled'),'category':p['category'],'src':p['image'],'order':p.get('order',100),'cover':p.get('cover',False)})
photos.sort(key=lambda p:(p['order'],p['title']))
site=json.loads((root/'content/site.json').read_text(encoding='utf-8'))
data={'site':site,'photos':photos,'categories':['Street','Landscapes','Other','Portraits','Travel','Carnies','Animals']}
(root/'gallery-data.js').write_text('window.PORTFOLIO_DATA = '+json.dumps(data,ensure_ascii=False)+';\n',encoding='utf-8')
print(f'Built gallery with {len(photos)} photographs')

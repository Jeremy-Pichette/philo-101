import re,json
def body(path,start,end):
    t=open(path).read()
    t=t[t.index(start):t.index(end)]
    t=re.sub(r'\n\s*\d\s*\n','\n',t)   # page numbers
    t=t.replace('\x0c','')
    return t
out={}
a=body('apo.txt','1Et ici quelqu','Source : Platon, Apologie')
paras=re.split(r'(?:^|\n)(\d)(?=[A-ZÀ-Ü])',a)
res=[]
for i in range(1,len(paras),2):
    res.append({'n':int(paras[i]),'text':re.sub(r'-\n(?=\w)','-',re.sub(r'\s*\n\s*',' ',paras[i+1])).strip()})
out['apologie']=res
c=body('cri.txt','1Socrate : Que viens','Source : Platon, Criton')
c=re.sub(r'\nPartie \d · [^\n]*\n','\n',c)
paras=re.split(r'(?:^|\n)(\d{1,3})(?=(?:Socrate|Criton|Tout d|Voilà|Réfléchis|Mais peut|Allons)\b)',c)
res=[]
for i in range(1,len(paras),2):
    txt=re.sub(r'\s*\n\s*',' ',paras[i+1]).strip()
    m=re.match(r'(Socrate|Criton) : (.*)',txt)
    res.append({'n':int(paras[i]),'who':m.group(1) if m else 'Les Lois','text':m.group(2) if m else txt})
out['criton']=res
json.dump(out,open('texts.json','w'),ensure_ascii=False,indent=0)
print(len(out['apologie']),[p['n'] for p in out['apologie']])
ns=[p['n'] for p in res]; print(len(res), ns==list(range(1,102)), [n for n in range(1,102) if n not in ns])
print(res[89]['who'], res[89]['text'][:80]); print(res[100])

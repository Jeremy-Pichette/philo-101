import json,sys,re
TR=sys.argv[1]; content=json.load(open(sys.argv[2])); out=sys.argv[3]
durs=[2158.2,2932.4]
def load(p):
    if p.endswith('.jsonl'): return [json.loads(l) for l in open(p) if l.strip()]
    return json.load(open(p))
fix=json.load(open('fixes.json')) if len(sys.argv)<5 else json.load(open(sys.argv[4]))
def clean(t):
    for a,b in fix.items(): t=re.sub(a,b,t)
    return t
parts=[]
for i,f in enumerate(content['files']):
    segs=load(TR+'/'+f)
    paras=[];cur=None;last_end=0
    chapters={int(k):v for k,v in content.get('chapters',[{},{}])[i].items()}
    for s in segs:
        txt=s['text'].strip()
        if not txt: continue
        brk = cur is None or (s['start']-last_end>2.5 and len(cur['text'])>200) or (len(cur['text'])>520 and re.search(r'[.?!»]$',cur['text'])) or len(cur['text'])>900
        ch=None
        for k in list(chapters):
            if s['start']>=k: ch=chapters.pop(k); brk=True
        if brk:
            if cur: paras.append(cur)
            cur={'t':s['start'],'text':txt}
            if ch: cur['chapter']=ch
        else: cur['text']+=' '+txt
        last_end=s['end']
    if cur: paras.append(cur)
    for p in paras: p['text']=clean(p['text'])
    parts.append({'title':content['partTitles'][i],'duration':durs[i],'paragraphs':paras})
data={'parts':parts,'texts':content['texts'],'essentiel':content['essentiel'],'cards':content['cards'],'quiz':content['quiz']}
html=open('template.html').read().replace('/*DATA*/null',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
open(out,'w').write(html)
print(out, len(html)//1024,'KB', [len(p['paragraphs']) for p in parts])

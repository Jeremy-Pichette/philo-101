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
            cur={'t':s['start'],'text':txt,'segs':[[s['start'],txt]]}
            if ch: cur['chapter']=ch
        else:
            cur['text']+=' '+txt; cur['segs'].append([s['start'],txt])
        last_end=s['end']
    if cur: paras.append(cur)
    for p in paras:
        p['segs']=[[t,clean(x)] for t,x in p['segs']]
        del p['text']
    parts.append({'title':content['partTitles'][i],'duration':durs[i],'audio':'audio/seance%d.m4a'%(i+1),'paragraphs':paras})
# Lecture des textes (synthèse vocale) : audio + instant de chaque phrase
import os
texts=content['texts']
tim=json.load(open('textes-timing.json')) if os.path.exists('textes-timing.json') else {}
for t,(key,short) in zip(texts,[('apologie','Apologie'),('criton','Criton')]):
    t['short']=short
    if key in tim:
        t['audio']='audio/'+tim[key].get('file','texte-%s.m4a'%key); t['duration']=tim[key]['duration']
        by={x['n']:x['sents'] for x in tim[key]['paras']}
        for para in t['paras']:
            if para['n'] in by:
                assert ' '.join(x for _,x in by[para['n']])==para['text'], para['n']
                para['sents']=by[para['n']]
slides=json.load(open('diapos.json')) if os.path.exists('diapos.json') else []
data={'parts':parts,'texts':texts,'slides':slides,'essentiel':content['essentiel'],'cards':content['cards'],'quiz':content['quiz']}
html=open('template.html').read().replace('/*DATA*/null',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
open(out,'w').write(html)
print(out, len(html)//1024,'KB', [len(p['paragraphs']) for p in parts])

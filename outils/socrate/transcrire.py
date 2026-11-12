import json
from faster_whisper import WhisperModel
P="Cours de philosophie sur Socrate. Platon, Xénophon, Aristophane, Les Nuées, la maïeutique, Xanthippe, Critias, Léon de Salamine, les Trente tyrans, Mélétos, Anytos, Lycon, Criton, l'Apologie de Socrate, la ciguë, Delphes, les sophistes."
m=WhisperModel("turbo",device="cpu",compute_type="int8",cpu_threads=4)
for name in ["n1","n2"]:
    segs,_=m.transcribe(name+".wav",language="fr",beam_size=5,vad_filter=True,vad_parameters=dict(threshold=0.2,min_silence_duration_ms=1000,speech_pad_ms=400),initial_prompt=P,condition_on_previous_text=False)
    with open(name+".jsonl","w") as f:
        for s in segs:
            f.write(json.dumps({"start":round(s.start,1),"end":round(s.end,1),"text":s.text.strip()},ensure_ascii=False)+"\n"); f.flush()
    print("FINISHED",name,flush=True)
print("DONE",flush=True)

"""Lecture audio des textes de Platon avec la voix Piper « Tom » (fr_FR, medium).
Chaque phrase est synthétisée séparément pour connaître son instant de départ exact :
le lecteur de l'app surligne la phrase lue (comme les « paroles en direct » du cours).
Sortie : <out>/texte-apologie.m4a, <out>/texte-criton.m4a et <out>/textes-timing.json
"""
import json, re, subprocess, sys, wave
import numpy as np
from piper import PiperVoice, SynthesisConfig

TEXTS, MODEL, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
voice = PiperVoice.load(MODEL)
SR = voice.config.sample_rate
CFG = SynthesisConfig(length_scale=1.08, noise_scale=0.6, noise_w_scale=0.8)
PAUSE_SENT, PAUSE_PARA, PAUSE_PART = 0.32, 0.7, 1.1

SPLIT = re.compile(r'(?<=[.!?…])\s+(?=[«"A-ZÀ-ÖØ-Þ(–—-])')

def spoken(t):
    t = t.replace('’', "'").replace('«', '').replace('»', '').replace('“', '').replace('”', '')
    t = re.sub(r'\s*[–—]\s*', ', ', t)          # incises du dialogue
    t = re.sub(r'\s+', ' ', t).strip(' ,')
    return t

def synth(text):
    chunks = [c.audio_int16_array for c in voice.synthesize(text, CFG)]
    return np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.int16)

def silence(s):
    return np.zeros(int(SR * s), dtype=np.int16)

def build(name, title, paras, parts=None):
    pieces, t, timing = [], 0.0, []
    def add(a):
        nonlocal t
        pieces.append(a); t += len(a) / SR
    add(synth(title)); add(silence(PAUSE_PART))
    for p in paras:
        n = p['n']
        if parts and str(n) in parts:
            if n != 1: add(silence(PAUSE_PART - PAUSE_PARA))
            add(synth(parts[str(n)])); add(silence(PAUSE_PARA))
        if p.get('who') in ('Socrate', 'Criton'):
            add(synth(p['who'] + '.')); add(silence(0.18))
        sents = [s for s in SPLIT.split(p['text']) if s.strip()]
        out = []
        for i, s in enumerate(sents):
            out.append([round(t, 2), s])
            add(synth(spoken(s)))
            add(silence(PAUSE_SENT if i < len(sents) - 1 else PAUSE_PARA))
        timing.append({'n': n, 'sents': out})
        print(name, n, round(t), flush=True)
    audio = np.concatenate(pieces)
    wav = f'{OUT}/{name}.wav'
    with wave.open(wav, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(audio.tobytes())
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11',
                    '-ac', '1', '-ar', '44100', '-c:a', 'aac', '-b:a', '56k', '-movflags', '+faststart',
                    '-metadata', f'title={title}', f'{OUT}/{name}.m4a'], check=True)
    return {'duration': round(len(audio) / SR, 2), 'paras': timing}

T = json.load(open(TEXTS))
res = {
    'apologie': build('texte-apologie', "Platon. Apologie de Socrate. Extrait de la première partie.", T['apologie']),
    'criton': build('texte-criton', "Platon. Criton.", T['criton'],
                    {'1': "Première partie. Les arguments de Criton.",
                     '35': "Deuxième partie. Les principes de Socrate.",
                     '85': "Troisième partie. Les Lois prennent la parole."}),
}
json.dump(res, open(f'{OUT}/textes-timing.json', 'w'), ensure_ascii=False)
print('DONE', {k: v['duration'] for k, v in res.items()})

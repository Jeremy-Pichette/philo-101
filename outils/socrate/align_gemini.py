"""Assemble les morceaux Gemini et retrouve l'instant de départ de chaque phrase.
faster-whisper donne l'horodatage de chaque mot entendu ; on aligne ces mots sur le texte connu
(difflib), puis chaque phrase prend l'instant de son premier mot reconnu.
Sortie : out_gem/texte-<nom>.m4a et out_gem/textes-timing.json (même format que la version Piper)."""
import difflib, json, os, re, subprocess, unicodedata, wave
import numpy as np
from faster_whisper import WhisperModel

SPLIT = re.compile(r'(?<=[.!?…])\s+(?=[«"A-ZÀ-ÖØ-Þ(–—-])')
GAP = 0.6  # silence entre deux morceaux (s)
os.makedirs('out_gem', exist_ok=True)
model = WhisperModel('turbo', device='cpu', compute_type='int8', cpu_threads=4)

def words(t):
    t = unicodedata.normalize('NFC', t.lower()).replace('’', "'")
    t = re.sub(r"[^\w']+", ' ', t)
    return [w for w in re.split(r"[\s']+", t) if w]

def read_wav(p):
    with wave.open(p) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16), w.getframerate()

def build(name, title):
    plan = json.load(open(f'gem/{name}-plan.json'))['chunks']
    audio, offset, paras = [], 0.0, []
    for ci, chunk in enumerate(plan):
        pcm, sr = read_wav(f'gem/{name}-{ci:02d}.wav')
        # mots de référence, avec (paragraphe, phrase) de chaque mot
        ref, owner, sents_of = [], [], {}
        for turn in chunk:
            n = turn['n']
            if n is None:
                for w in words(turn['text']): ref.append(w); owner.append(None)
                continue
            sents = [s for s in SPLIT.split(turn['text']) if s.strip()]
            sents_of[n] = sents
            for si, s in enumerate(sents):
                for w in words(s): ref.append(w); owner.append((n, si))
        segs, _ = model.transcribe(f'gem/{name}-{ci:02d}.wav', language='fr', beam_size=1, word_timestamps=True,
                                   condition_on_previous_text=False, vad_filter=False)
        hyp, hyp_t = [], []
        for s in segs:
            for w in s.words:
                for x in words(w.word):
                    hyp.append(x); hyp_t.append(w.start)
        sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
        t_of = {}
        for a, b, size in sm.get_matching_blocks():
            for k in range(size): t_of[a + k] = hyp_t[b + k]
        matched = len(t_of) / max(1, len(ref))
        # instant de départ de chaque phrase
        starts = {}
        for idx, o in enumerate(owner):
            if o is None or o in starts: continue
            # premier mot reconnu de la phrase ; on recule d'environ 0,32 s par mot manqué avant lui
            j, miss = idx, 0
            while j < len(owner) and owner[j] == o and j not in t_of: j += 1; miss += 1
            if j < len(owner) and owner[j] == o: starts[o] = max(0.0, t_of[j] - 0.32 * miss)
        # phrases sans aucun mot reconnu : interpolées entre leurs voisines
        keys = [o for o in dict.fromkeys(x for x in owner if x is not None)]
        for i, o in enumerate(keys):
            if o in starts: continue
            prev = next((starts[k] for k in reversed(keys[:i]) if k in starts), 0.0)
            nxt = next((starts[k] for k in keys[i + 1:] if k in starts), len(pcm) / sr)
            starts[o] = prev + (nxt - prev) * 0.5
        # monotonie
        last = 0.0
        for o in keys:
            starts[o] = max(starts[o], last); last = starts[o]
        for n, sents in sents_of.items():
            paras.append({'n': n, 'sents': [[round(offset + starts[(n, si)] - 0.08, 2) if starts[(n, si)] > 0.1 else round(offset + starts[(n, si)], 2), s] for si, s in enumerate(sents)]})
        print(name, ci, f'mots reconnus {matched:.0%}', flush=True)
        audio += [pcm, np.zeros(int(sr * GAP), dtype=np.int16)]
        offset += len(pcm) / sr + GAP
    full = np.concatenate(audio[:-1])
    wav = f'out_gem/{name}.wav'
    with wave.open(wav, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(full.tobytes())
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11', '-ac', '1',
                    '-ar', '44100', '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', '-metadata', f'title={title}',
                    f'out_gem/texte-{name}.m4a'], check=True)
    paras.sort(key=lambda p: p['n'])
    return {'duration': round(len(full) / sr, 2), 'paras': paras}

import sys
TITLES = {'apologie': 'Platon · Apologie de Socrate', 'criton': 'Platon · Criton'}
path = 'out_gem/textes-timing.json'
res = json.load(open(path)) if os.path.exists(path) else {}
for name in (sys.argv[1:] or TITLES):
    res[name] = build(name, TITLES[name])
    json.dump(res, open(path, 'w'), ensure_ascii=False)
print('DONE', {k: v['duration'] for k, v in res.items()})

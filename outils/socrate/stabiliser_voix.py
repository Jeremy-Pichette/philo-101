"""Stabilise la hauteur des voix d'une réplique à l'autre, sans régénérer.
- Répliques : paragraphes de textes-timing.json ; locuteur d'après texts.json (« Les Lois » = voix de Socrate).
- Fin d'une réplique = dernier mot (words.json) + 0,7 s, sans dépasser la réplique suivante.
- Hauteur : F0 médiane (parselmouth / Praat) en demi-tons ; référence = médiane pondérée par personnage, sur les deux textes.
- Correction : seulement si l'écart dépasse 1 demi-ton ; on ramène à ±0,5 demi-ton de la référence, plafond 3 demi-tons.
  rubberband -F (formants préservés), durée identique, fondus de 25 ms aux raccords.
Usage : python3 pitch_fix.py <textes-timing.json> <words.json> <texts.json> <dossier sortie>"""
import json, os, subprocess, sys, tempfile, wave
import numpy as np, parselmouth

TIMING, WORDS, TEXTS, OUT = sys.argv[1:5]
os.makedirs(OUT, exist_ok=True)
tim, words, texts = json.load(open(TIMING)), json.load(open(WORDS)), json.load(open(TEXTS))
SRC = {'apologie': ('t0', 'out_gem/apologie.wav'), 'criton': ('t1', 'out_gem/criton.wav')}

def read(p):
    with wave.open(p) as w: return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768, w.getframerate()

def f0_stats(x, sr):
    if len(x) < sr * 0.3: return None, 0
    pitch = parselmouth.Sound(x.astype(np.float64), sr).to_pitch_ac(time_step=0.01, pitch_floor=60, pitch_ceiling=400)
    f = pitch.selected_array['frequency']; f = f[f > 0]
    if len(f) < 20: return None, len(f)
    return float(np.median(12 * np.log2(f / 100))), len(f)

segs, audio = [], {}
for name, (key, path) in SRC.items():
    x, sr = read(path); audio[name] = (x, sr)
    who = {p['n']: ('Socrate' if p.get('who') in (None, 'Socrate', 'Les Lois') else p['who']) for p in texts[name]}
    paras = sorted(tim[name]['paras'], key=lambda p: p['n'])
    flat_w = words.get(key, [])
    k = 0; ends = []
    for p in paras:                      # fin = dernier mot de la dernière phrase + 0,7 s
        last = p['sents'][-1]; w = flat_w[k + len(p['sents']) - 1] if k + len(p['sents']) - 1 < len(flat_w) else None
        ends.append(last[0] + (w[-1] / 100 if w else 2.0) + 0.7); k += len(p['sents'])
    for i, p in enumerate(paras):
        a = max(0.0, p['sents'][0][0]); nxt = paras[i + 1]['sents'][0][0] if i + 1 < len(paras) else len(x) / sr
        b = min(ends[i], nxt)
        med, n = f0_stats(x[int(a * sr):int(b * sr)], sr)
        segs.append({'text': name, 'n': p['n'], 'who': who.get(p['n'], 'Socrate'), 'a': a, 'b': b, 'f0': med, 'frames': n})

refs = {}
for spk in sorted({s['who'] for s in segs}):
    v = [(s['f0'], s['frames']) for s in segs if s['who'] == spk and s['f0'] is not None]
    vals = np.repeat([x for x, _ in v], [max(1, n // 10) for _, n in v])
    refs[spk] = float(np.median(vals))

def shift_for(s):
    if s['f0'] is None: return 0.0
    d = s['f0'] - refs[s['who']]
    if abs(d) <= 1.0: return 0.0
    return float(np.clip(-(d - np.sign(d) * 0.5), -3, 3))

report = {}
for name, (x, sr) in audio.items():
    y = x.copy()
    for s in [s for s in segs if s['text'] == name]:
        s['shift'] = shift_for(s)
        if not s['shift']: continue
        i0, i1 = int(s['a'] * sr), int(s['b'] * sr)
        part = x[i0:i1]
        with tempfile.TemporaryDirectory() as td:
            fi, fo = os.path.join(td, 'i.wav'), os.path.join(td, 'o.wav')
            with wave.open(fi, 'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(part, -1, 1) * 32767).astype(np.int16).tobytes())
            subprocess.run(['rubberband', '--fine', '-F', '-p', f"{s['shift']:.3f}", '-q', fi, fo], check=True, capture_output=True)
            z, _ = read(fo)
        z = np.pad(z, (0, max(0, len(part) - len(z))))[:len(part)]
        fade = min(int(sr * 0.025), len(part) // 4)
        ramp = np.linspace(0, 1, fade)
        z[:fade] = z[:fade] * ramp + part[:fade] * (1 - ramp)
        z[-fade:] = z[-fade:] * ramp[::-1] + part[-fade:] * (1 - ramp[::-1])
        y[i0:i1] = z
    wav = f'{OUT}/{name}.wav'
    with wave.open(wav, 'wb') as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-af', 'loudnorm=I=-18:TP=-1.5:LRA=11', '-ac', '1', '-ar', '44100',
                    '-c:a', 'aac', '-b:a', '64k', '-movflags', '+faststart', f'{OUT}/texte-{name}-gemini-v2.m4a'], check=True)
    # mesure après correction
    for s in [s for s in segs if s['text'] == name]:
        s['f0_after'], _ = f0_stats(y[int(s['a'] * sr):int(s['b'] * sr)], sr)

for spk, ref in refs.items():
    b = np.array([s['f0'] - ref for s in segs if s['who'] == spk and s['f0'] is not None])
    a = np.array([s['f0_after'] - ref for s in segs if s['who'] == spk and s.get('f0_after') is not None])
    corr = [s for s in segs if s['who'] == spk and s.get('shift')]
    report[spk] = {'référence_Hz': round(100 * 2 ** (ref / 12), 1), 'répliques': int(len(b)), 'corrigées': len(corr),
                   'écart_type_avant_dt': round(float(b.std()), 2), 'écart_type_après_dt': round(float(a.std()), 2),
                   'écart_max_avant_dt': round(float(np.abs(b).max()), 2), 'écart_max_après_dt': round(float(np.abs(a).max()), 2)}
json.dump({'refs': refs, 'segs': segs, 'report': report}, open(f'{OUT}/pitch-report.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(report, ensure_ascii=False, indent=1))
top = sorted([s for s in segs if s.get('shift')], key=lambda s: -abs(s['shift']))[:6]
for s in top: print(s['text'], '§', s['n'], s['who'], 'écart', round(s['f0'] - refs[s['who']], 2), 'dt → décalage', round(s['shift'], 2))

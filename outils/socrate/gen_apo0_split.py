"""Génère le morceau 0 de l'Apologie en deux requêtes plus courtes, puis les assemble dans gem/apologie-00.wav
(le plan de découpage, gem/apologie-plan.json, reste identique : mêmes répliques, même ordre)."""
import io, os, struct, sys, wave
sys.path.insert(0, os.path.dirname(__file__))
from gemini import call_stream, turns_body
from gen_gemini import chunks, VOICES

c = chunks('apologie')[0]
halves = [c[:3], c[3:]]          # titre + § 1-2 | § 3-4
pcm = bytearray()
for h in halves:
    chars = sum(len(x[1]) for x in h)
    for attempt in range(3):
        a = call_stream(turns_body([(s, t, st) for s, t, st, _ in h], {'Socrate': VOICES['Socrate']}))
        dur = (len(a) - 44) / 48000
        print(len(h), 'répliques,', chars, 'car. ->', round(dur, 1), 's', flush=True)
        if dur >= chars / 24: break
    else:
        raise SystemExit('toujours tronqué')
    pcm += a[44:] + bytes(int(24000 * 0.5) * 2)   # 0,5 s de silence entre les deux moitiés
hdr = b'RIFF' + struct.pack('<I', 36 + len(pcm)) + b'WAVEfmt ' + struct.pack('<IHHIIHH', 16, 1, 1, 24000, 48000, 2, 16) + b'data' + struct.pack('<I', len(pcm))
open('gem/apologie-00.wav', 'wb').write(hdr + bytes(pcm))
print('ok', round(len(pcm) / 48000, 1), 's')

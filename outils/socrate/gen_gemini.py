"""Lecture expressive de l'Apologie et du Criton avec Gemini TTS.
- Criton : deux voix (Socrate, Criton) ; les Lois parlent par la voix de Socrate, sur un ton solennel.
- Apologie : la voix de Socrate devant ses juges.
- Chaque réplique reçoit une consigne de jeu (style) tirée de son contenu.
- Les textes sont groupés en grands morceaux (quota gratuit limité) ; chaque morceau est mis en cache.
Usage : python3 gen_gemini.py plan | gen <texte> [indices…]
"""
import json, os, sys, wave, io
sys.path.insert(0, os.path.dirname(__file__))
from gemini import call_stream, turns_body

VOICES = {'Socrate': 'Charon', 'Criton': 'Fenrir'}
MAX_CHARS = 4200
T = json.load(open(os.path.join(os.path.dirname(__file__), 'texts.json')))

SOCRATE = "an elderly Athenian philosopher, calm, serene and warm, unhurried, with gentle irony; natural French delivery"
CRITON = "an old loyal friend, anxious and emotional, pleading, slightly faster pace; natural French delivery"
LOIS = "solemn, grave and authoritative, slower and majestic, as if the Laws of Athens themselves were speaking"
TITLE = "neutral, clear announcement, like the title of an audiobook chapter"

APO = {
    0: "an elderly Athenian philosopher defending himself before a large popular jury; calm, confident, measured, with gentle irony; natural French delivery",
    1: "quoting an imagined objector from the crowd, slightly mocking and curious",
    2: "earnest and reassuring, promising to tell only the truth",
    3: "earnest, building suspense; slower and weightier when revealing the oracle's answer",
    4: "reflective and puzzled at first, then recounting his inquiry with dry humour",
    5: "sincere, a touch of sadness at the hatred he earned, then firm resolve",
    6: "amused irony about the poets, slightly embarrassed to tell the truth",
    7: "respectful of the craftsmen's skill, then gently disappointed by their presumption",
    8: "solemn and conclusive, humble yet firm; slower on the final lesson about human wisdom",
}
CRI_SOC = {
    range(1, 14): "calm, a little drowsy, kind and surprised to see his friend at dawn",
    range(15, 26): "serene, almost dreamy, softly recounting a vision",
    range(27, 30): "gently ironic and philosophical",
    range(31, 32): "kind but evasive",
    range(35, 36): "warm but firm, deliberate, reasoning carefully",
    range(36, 71): "patient Socratic questioning, clear and logical",
    range(71, 72): "earnest and intense, insisting on the principle",
    range(72, 81): "patient and clear",
    range(81, 82): "grave and serious, a solemn warning",
    range(83, 86): "patient, leading the argument step by step",
    range(87, 99): LOIS,
    range(99, 100): "quiet, intimate and deeply convinced, almost whispering",
    range(101, 102): "peaceful, final and serene",
}
CRI_CRI = {
    range(1, 14): "hushed, sad and tender, speaking softly in a prison at dawn",
    range(14, 17): "heavy and grieving, announcing terrible news",
    range(18, 25): "puzzled and uneasy",
    range(26, 27): "desperate and pleading, voice almost breaking",
    range(28, 29): "bitter and insistent",
    range(30, 33): "insistent and reassuring, speaking fast",
    range(33, 35): "reproachful and passionate, urgent, rushing at the end",
    range(36, 85): "attentive and calmer, simply agreeing",
    range(86, 87): "confused, hesitant",
    range(88, 99): "convinced, quietly agreeing",
    range(100, 101): "resigned and defeated, softly",
}
PARTS = {1: "Première partie. Les arguments de Criton.", 35: "Deuxième partie. Les principes de Socrate.", 85: "Troisième partie. Les Lois prennent la parole."}

def pick(table, n, default):
    for r, s in table.items():
        if n in r: return s
    return default

def turns_for(name):
    """[(speaker, text, style, para_n or None)]"""
    out = []
    if name == 'apologie':
        out.append(('Socrate', "Platon. Apologie de Socrate. Extrait de la première partie.", TITLE, None))
        for p in T['apologie']:
            out.append(('Socrate', p['text'], APO[0] + '; ' + APO.get(p['n'], ''), p['n']))
    else:
        out.append(('Socrate', "Platon. Criton.", TITLE, None))
        for p in T['criton']:
            n = p['n']
            if n in PARTS: out.append(('Socrate', PARTS[n], TITLE, None))
            who = p['who'] if p['who'] in VOICES else 'Socrate'
            if who == 'Criton': style = CRITON + '; ' + pick(CRI_CRI, n, '')
            elif p['who'] == 'Les Lois': style = LOIS
            else: style = SOCRATE + '; ' + pick(CRI_SOC, n, '')
            out.append((who, p['text'], style, n))
    return out

def chunks(name):
    # blocs insécables : un titre reste avec le paragraphe qui le suit
    blocks, pending = [], []
    for t in turns_for(name):
        pending.append(t)
        if t[3] is not None: blocks.append(pending); pending = []
    if pending: blocks.append(pending)
    res, cur, size = [], [], 0
    for b in blocks:
        bs = sum(len(t[1]) for t in b)
        if cur and size + bs > MAX_CHARS:
            res.append(cur); cur, size = [], 0
        cur += b; size += bs
    if cur: res.append(cur)
    return res

def gen(name, idxs=None):
    os.makedirs('gem', exist_ok=True)
    cs = chunks(name)
    for i, c in enumerate(cs):
        if idxs and i not in idxs: continue
        path = f'gem/{name}-{i:02d}.wav'
        if os.path.exists(path): print('cached', path); continue
        voices = VOICES if name == 'criton' else {'Socrate': VOICES['Socrate']}
        body = turns_body([(s, t, st) for s, t, st, _ in c], voices)
        print(f'{name} chunk {i}: {len(c)} turns, {sum(len(x[1]) for x in c)} chars …', flush=True)
        chars = sum(len(x[1]) for x in c)
        for attempt in range(3):
            a = call_stream(body)
            dur = (len(a) - 44) / 48000
            if dur >= chars / 24: break   # ~16 car./s attendus : en dessous de 24 car./s, l'audio est tronqué
            print(f'  tronqué ({dur:.0f} s pour {chars} car.), nouvel essai', flush=True)
        else:
            raise SystemExit(f'{name} {i}: audio toujours tronqué')
        open(path, 'wb').write(a)
        with wave.open(io.BytesIO(a)) as w: print('  ->', round(w.getnframes() / w.getframerate(), 1), 's', flush=True)
    json.dump({'chunks': [[{'speaker': s, 'n': n, 'text': t} for s, t, _, n in c] for c in cs]},
              open(f'gem/{name}-plan.json', 'w'), ensure_ascii=False)

if __name__ == '__main__':
    if sys.argv[1] == 'plan':
        for name in ('apologie', 'criton'):
            cs = chunks(name)
            print(name, len(cs), 'chunks', [sum(len(t[1]) for t in c) for c in cs], [ (c[0][3], c[-1][3]) for c in cs])
    else:
        gen(sys.argv[2], set(map(int, sys.argv[3:])) or None)

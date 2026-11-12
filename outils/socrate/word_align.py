"""Horodatage mot à mot pour les « paroles en direct ».
Pour chaque audio, faster-whisper donne l'instant de chaque mot entendu ; on aligne ces mots sur le texte
affiché (difflib), puis chaque mot du texte prend l'instant du mot reconnu correspondant. Les mots non
reconnus sont interpolés entre leurs voisins, dans les bornes de leur phrase.
Sortie : words.json = { clé: [[offsets en centisecondes depuis le début de la phrase, un par mot], …] }
dans l'ordre des phrases fournies."""
import difflib, json, re, sys, unicodedata
from faster_whisper import WhisperModel

def norm_units(tok):
    t = unicodedata.normalize('NFC', tok.lower()).replace('’', "'")
    t = re.sub(r"[^\w']+", ' ', t)
    return [w for w in re.split(r"[\s']+", t) if w]

def align(model, audio, sentences, vad):
    """sentences: [(t_abs, text)] -> [[offset_cs, …] par phrase]"""
    segs, _ = model.transcribe(audio, language='fr', beam_size=1, word_timestamps=True, condition_on_previous_text=False,
                               vad_filter=vad, vad_parameters=dict(threshold=0.2, min_silence_duration_ms=1000, speech_pad_ms=400) if vad else None)
    hyp, hyp_t = [], []
    for s in segs:
        for w in s.words:
            for u in norm_units(w.word): hyp.append(u); hyp_t.append(w.start)
    ref, owner = [], []          # owner = (phrase, mot)
    toks = [t.split(' ') for _, t in sentences]
    for si, tk in enumerate(toks):
        for wi, tok in enumerate(tk):
            for u in norm_units(tok): ref.append(u); owner.append((si, wi))
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    t_of = {}
    for a, b, n in sm.get_matching_blocks():
        for k in range(n): t_of[a + k] = hyp_t[b + k]
    word_t = {}
    for i, o in enumerate(owner):
        if i in t_of and o not in word_t: word_t[o] = t_of[i]
    out, matched, total = [], 0, 0
    ends = [t for t, _ in sentences[1:]] + [sentences[-1][0] + 30]
    for si, tk in enumerate(toks):
        start, end = sentences[si][0], max(sentences[si][0] + 0.3, ends[si])
        times = [word_t.get((si, wi)) for wi in range(len(tk))]
        # garder seulement les instants plausibles et croissants dans la phrase
        last = start
        for wi, x in enumerate(times):
            if x is None or x < start - 0.6 or x > end + 0.3 or x < last: times[wi] = None
            else: last = x
        matched += sum(x is not None for x in times); total += len(times)
        # interpolation des trous (proportionnelle au nombre de caractères)
        known = [(-1, start)] + [(wi, x) for wi, x in enumerate(times) if x is not None] + [(len(tk), end)]
        for (ia, ta), (ib, tb) in zip(known, known[1:]):
            gap = list(range(ia + 1, ib))
            if not gap: continue
            w = [len(tk[k]) + 1 for k in range(max(ia, 0) if ia >= 0 else 0, ib)] if ia >= 0 else [len(tk[k]) + 1 for k in range(0, ib)]
            span, acc = tb - ta, 0
            weights = [len(tk[k]) + 1 for k in gap]
            base = (len(tk[ia]) + 1) if ia >= 0 else 0
            tot = base + sum(weights)
            acc = base
            for k, wk in zip(gap, weights):
                times[k] = ta + span * acc / tot; acc += wk
        times[0] = max(times[0], start) if times else start
        out.append([max(0, round((x - start) * 100)) for x in times])
    print(audio, f'mots reconnus {matched / max(1, total):.0%}', flush=True)
    return out

if __name__ == '__main__':
    jobs = json.load(open(sys.argv[1]))   # [{key, audio, vad, sentences:[[t, text]]}]
    model = WhisperModel('turbo', device='cpu', compute_type='int8', cpu_threads=4)
    res = {}
    for j in jobs:
        res[j['key']] = align(model, j['audio'], [tuple(x) for x in j['sentences']], j.get('vad', False))
        json.dump(res, open(sys.argv[2], 'w'))
    print('DONE')

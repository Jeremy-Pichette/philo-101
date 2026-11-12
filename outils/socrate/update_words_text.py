"""Recalcule l'horodatage mot à mot d'un texte lu (t0 = Apologie, t1 = Criton) et le fusionne dans words.json.
Usage : python3 update_words_text.py t0 <audio.wav> <textes-timing.json>"""
import json, sys
from faster_whisper import WhisperModel
from word_align import align

key, audio, timing = sys.argv[1], sys.argv[2], sys.argv[3]
name = {'t0': 'apologie', 't1': 'criton'}[key]
T = json.load(open(timing))[name]
sentences = [tuple(s[:2]) for p in sorted(T['paras'], key=lambda p: p['n']) for s in p['sents']]
model = WhisperModel('turbo', device='cpu', compute_type='int8', cpu_threads=4)
words = json.load(open('words.json'))
words[key] = align(model, audio, sentences, False)
json.dump(words, open('words.json', 'w'))
print('ok', key, len(words[key]))

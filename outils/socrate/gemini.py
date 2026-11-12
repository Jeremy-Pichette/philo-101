"""Appel minimal à Gemini TTS (API Interactions). La clé est injectée par le proxy de l'environnement."""
import base64, json, sys, time, urllib.request, urllib.error

URL = 'https://generativelanguage.googleapis.com/v1beta/interactions'
MODEL = 'gemini-3.8-flash-tts'

def call(body, raw_out=None, retries=6):
    data = json.dumps(body).encode()
    for attempt in range(retries):
        req = urllib.request.Request(URL, data=data, method='POST',
                                     headers={'Content-Type': 'application/json', 'x-goog-api-key': 'injected-by-proxy'})
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                resp = json.load(r)
            if raw_out:
                json.dump(resp, open(raw_out, 'w'), indent=1)
            return resp
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:600]
            print('HTTP', e.code, msg, file=sys.stderr, flush=True)
            if e.code in (429, 500, 503) and attempt < retries - 1:
                wait = 30 * (attempt + 1)
                m = __import__('re').search(r'retry in ([\d.]+)s', msg)
                if m: wait = float(m.group(1)) + 2
                print('retry in', wait, file=sys.stderr, flush=True); time.sleep(wait); continue
            raise

def call_stream(body, retries=6):
    """Requête en flux (SSE) : la connexion reste active pendant toute la génération. Renvoie du WAV 24 kHz."""
    import re, struct
    body = dict(body, stream=True)
    data = json.dumps(body).encode()
    for attempt in range(retries):
        req = urllib.request.Request(URL, data=data, method='POST',
                                     headers={'Content-Type': 'application/json', 'Accept': 'text/event-stream',
                                              'x-goog-api-key': 'injected-by-proxy'})
        pcm = bytearray(); errs = []
        try:
            with urllib.request.urlopen(req, timeout=900) as r:
                for line in r:
                    line = line.decode('utf-8', 'replace').strip()
                    if not line.startswith('data:'): continue
                    payload = line[5:].strip()
                    if not payload or payload == '[DONE]': continue
                    ev = json.loads(payload)
                    d = ev.get('delta') or {}
                    if d.get('type') == 'audio' and d.get('data'):
                        pcm += base64.b64decode(d['data'])
                    elif 'error' in ev:
                        errs.append(ev['error'])
            if errs: raise RuntimeError(errs)
            if not pcm: raise RuntimeError('aucun audio reçu')
            hdr = b'RIFF' + struct.pack('<I', 36 + len(pcm)) + b'WAVEfmt ' + struct.pack('<IHHIIHH', 16, 1, 1, 24000, 48000, 2, 16) + b'data' + struct.pack('<I', len(pcm))
            return hdr + bytes(pcm)
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:600]
            print('HTTP', e.code, msg, file=sys.stderr, flush=True)
            if e.code in (429, 500, 502, 503) and attempt < retries - 1:
                wait = 30 * (attempt + 1)
                m = re.search(r'retry in ([\d.]+)s', msg)
                if m: wait = float(m.group(1)) + 2
                print('retry in', wait, file=sys.stderr, flush=True); time.sleep(wait); continue
            raise

def find_audio(obj):
    """Cherche récursivement des données audio base64 dans la réponse."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ('data', 'audio', 'inline_data', 'inlineData') and isinstance(v, str) and len(v) > 1000:
                return base64.b64decode(v)
            r = find_audio(v)
            if r: return r
    elif isinstance(obj, list):
        for v in obj:
            r = find_audio(v)
            if r: return r
    return None

def turns_body(turns, voices):
    """turns: [(speaker, text, style)] ; voices: {speaker: voice}. 1 voix -> single speaker."""
    content = []
    for spk, text, style in turns:
        meta = {'type': 'speech_metadata'}
        if len(voices) > 1: meta['speaker'] = spk
        if style: meta['style'] = style
        item = {'type': 'text', 'text': text}
        if len(meta) > 1: item['annotations'] = [meta]
        content.append(item)
    speech = ({'speakers': [{'speaker': s, 'voice': v} for s, v in voices.items()]} if len(voices) > 1
              else [{'voice': list(voices.values())[0]}])
    return {'model': MODEL, 'input': [{'type': 'user_input', 'content': content}],
            'response_format': {'type': 'audio'}, 'generation_config': {'speech_config': speech}}

if __name__ == '__main__':
    body = turns_body([('Socrate', "Que viens-tu faire ici à cette heure, Criton ? N’est-ce pas encore bien matin ?", 'calm, warm, a bit sleepy, gently surprised'),
                       ('Criton', "Si.", 'tense, whispering, worried')], {'Socrate': 'Charon', 'Criton': 'Fenrir'})
    resp = call(body, raw_out=sys.argv[1] + '.json')
    a = find_audio(resp)
    print('audio bytes', len(a) if a else None, a[:4] if a else None)
    if a: open(sys.argv[1] + '.wav', 'wb').write(a)

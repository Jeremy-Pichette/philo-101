/* Philo 101 — service worker
   - Pages HTML : réseau d'abord (pour recevoir les mises à jour), cache si hors ligne
   - Autres fichiers (icônes, PDF, manifestes) : cache d'abord, mise à jour en arrière-plan
   - Audios : servis depuis le cache « hors ligne » s'ils ont été téléchargés (avec gestion des requêtes Range,
     indispensable à Safari), sinon directement depuis le réseau. */
const VERSION = '2026-11-12-6';
const CORE = 'philo-core-' + VERSION;
const RUNTIME = 'philo-runtime';
const AUDIO = 'philo-audio';

const PRECACHE = [
  './',
  'index.html',
  'manifest.webmanifest',
  'icons/apple-touch-icon.png',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/favicon-32.png',
  'socrate/',
  'socrate/index.html',
  'socrate/icons/icon-192.png',
  'socrate/transcription.html'
];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CORE);
    // Chaque fichier séparément : un fichier manquant ne bloque pas l'installation.
    await Promise.all(PRECACHE.map(u => cache.add(new Request(u, { cache: 'reload' })).catch(() => {})));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k.startsWith('philo-core-') && k !== CORE).map(k => caches.delete(k)));
    if (self.registration.navigationPreload) { try { await self.registration.navigationPreload.enable(); } catch (e) {} }
    await self.clients.claim();
  })());
});

self.addEventListener('message', event => {
  if (event.data === 'skipWaiting') self.skipWaiting();
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  if (/\.(m4a|mp3|aac|mp4)$/i.test(url.pathname)) {
    event.respondWith(audioResponse(req, url));
    return;
  }
  const isHTML = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  if (isHTML) {
    event.respondWith(networkFirst(event, req));
    return;
  }
  event.respondWith(staleWhileRevalidate(event, req));
});

async function networkFirst(event, req) {
  const cache = await caches.open(CORE);
  try {
    const preload = event.preloadResponse ? await event.preloadResponse : null;
    const res = preload || await fetchWithTimeout(req, 4000);
    if (res && res.ok) cache.put(req, res.clone());
    return res;
  } catch (e) {
    const hit = await caches.match(req, { ignoreSearch: true })
      || await caches.match(new URL('index.html', req.url).href)
      || await caches.match(new URL('./', self.registration.scope).href);
    return hit || new Response('<h1>Hors ligne</h1><p>Cette page n’a pas encore été enregistrée.</p>', { headers: { 'Content-Type': 'text/html; charset=utf-8' } });
  }
}

async function staleWhileRevalidate(event, req) {
  const hit = await caches.match(req, { ignoreSearch: true });
  const update = fetch(req).then(async res => {
    if (res && res.ok && res.type === 'basic') (await caches.open(RUNTIME)).put(req, res.clone());
    return res;
  }).catch(() => null);
  if (hit) { event.waitUntil(update); return hit; }
  return (await update) || new Response('', { status: 504 });
}

function fetchWithTimeout(req, ms) {
  return new Promise((resolve, reject) => {
    const t = setTimeout(() => reject(new Error('timeout')), ms);
    fetch(req).then(r => { clearTimeout(t); resolve(r); }, err => { clearTimeout(t); reject(err); });
  });
}

async function audioResponse(req, url) {
  const cache = await caches.open(AUDIO);
  const cached = await cache.match(url.origin + url.pathname);
  if (!cached) return fetch(req);
  const range = req.headers.get('range');
  if (!range) return cached;
  const blob = await cached.blob();
  const size = blob.size;
  const m = /bytes=(\d*)-(\d*)/.exec(range);
  let start = m && m[1] ? parseInt(m[1], 10) : 0;
  let end = m && m[2] ? parseInt(m[2], 10) : size - 1;
  if (m && !m[1] && m[2]) { start = size - parseInt(m[2], 10); end = size - 1; }
  if (start >= size) return new Response('', { status: 416, headers: { 'Content-Range': `bytes */${size}` } });
  end = Math.min(end, size - 1);
  return new Response(blob.slice(start, end + 1), {
    status: 206,
    statusText: 'Partial Content',
    headers: {
      'Content-Type': cached.headers.get('Content-Type') || 'audio/mp4',
      'Content-Range': `bytes ${start}-${end}/${size}`,
      'Content-Length': String(end - start + 1),
      'Accept-Ranges': 'bytes'
    }
  });
}

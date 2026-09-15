const CACHE_NAME = 'chiikawa-tulevo-v2';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './style.css',
  './manifest.json',
  './src/main.js',
  './src/input.js',
  './src/character.js',
  './src/camera.js',
  './src/weapons.js',
  './src/hitboxes.js',
  './src/map.js',
  './src/bots.js',
  './src/ui.js',
  './src/audio.js',
  './src/mobile_controls.js',
  './src/hud_customizer.js',
  './libs/three.min.js',
  './libs/fflate.min.js',
  './libs/FBXLoader.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).catch(err => console.log('SW cache partial:', err))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request)
      .then((response) => {
        if (response && response.status === 200 && event.request.method === 'GET') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});

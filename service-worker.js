const CACHE_NAME = "dash-pwa-cache";
const urlsToCache = [
  "/",
  "/assets/manifest.json",
  "/assets/icon-192x192.png",
  "/assets/icon-512x512.png"
];

// Install the service worker and cache assets
self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Serve cached content when offline
self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

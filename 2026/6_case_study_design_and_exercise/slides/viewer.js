'use strict';
const slides = [...document.querySelectorAll('.slide')];
const stage = document.getElementById('stage');
const deck = document.getElementById('deck');
const page = document.getElementById('page');
const previous = document.getElementById('prev');
const next = document.getElementById('next');
const fullscreen = document.getElementById('fullscreen');
let current = 1;
if (new URLSearchParams(location.search).has('export')) document.body.classList.add('export');
function resize() {
  deck.style.setProperty('--scale', Math.min(stage.clientWidth / 1600, stage.clientHeight / 900));
}
function show(value) {
  const n = Number(value);
  current = Number.isFinite(n) ? Math.max(1, Math.min(slides.length, Math.trunc(n) || 1)) : 1;
  slides.forEach((slide, i) => { slide.hidden = i !== current - 1; });
  page.value = current;
  previous.disabled = current === 1;
  next.disabled = current === slides.length;
  document.title = `${current} / ${slides.length} — ${slides[current - 1].dataset.title}`;
  document.getElementById('status').textContent = document.title;
  if (location.hash !== `#${current}`) location.replace(`#${current}`);
}
function toggleBar() { document.body.classList.toggle('presentation'); resize(); }
async function toggleFullscreen() {
  try {
    if (document.fullscreenElement) await document.exitFullscreen();
    else if (document.documentElement.requestFullscreen) await document.documentElement.requestFullscreen();
    else toggleBar();
  } catch { toggleBar(); }
}
previous.addEventListener('click', () => show(current - 1));
next.addEventListener('click', () => show(current + 1));
page.addEventListener('change', () => show(page.value));
fullscreen.addEventListener('click', toggleFullscreen);
window.addEventListener('hashchange', () => {
  if (location.hash !== `#${current}`) show(location.hash.slice(1));
});
new ResizeObserver(resize).observe(stage);
document.addEventListener('fullscreenchange', () => {
  document.body.classList.toggle('presentation', Boolean(document.fullscreenElement));
  fullscreen.textContent = document.fullscreenElement ? '全画面を終了' : '全画面';
  resize();
});
document.addEventListener('keydown', event => {
  if (event.target.matches('input, textarea, select') || event.target.isContentEditable || event.ctrlKey || event.metaKey || event.altKey) return;
  if (event.target.closest('button, a') && (event.key === ' ' || event.key === 'Enter')) return;
  switch (event.key) {
    case 'ArrowRight': case 'ArrowDown': case 'PageDown': show(current + 1); break;
    case ' ': show(current + (event.shiftKey ? -1 : 1)); break;
    case 'ArrowLeft': case 'ArrowUp': case 'PageUp': show(current - 1); break;
    case 'Home': show(1); break;
    case 'End': show(slides.length); break;
    case 'f': case 'F': toggleFullscreen(); break;
    case 'h': case 'H': toggleBar(); break;
    case 'Escape': document.body.classList.remove('presentation'); resize(); break;
    default: return;
  }
  event.preventDefault();
});
let start = null;
stage.addEventListener('touchstart', event => {
  start = event.touches.length === 1 && !event.target.closest('a,button,input') ? { x: event.touches[0].clientX, y: event.touches[0].clientY } : null;
}, { passive: true });
stage.addEventListener('touchend', event => {
  if (!start || !event.changedTouches.length) return;
  const dx = event.changedTouches[0].clientX - start.x;
  const dy = event.changedTouches[0].clientY - start.y;
  if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy)) show(current + (dx < 0 ? 1 : -1));
  start = null;
}, { passive: true });
stage.addEventListener('touchcancel', () => { start = null; }, { passive: true });
show(location.hash.slice(1));
resize();

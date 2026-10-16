// FDCA - interações compartilhadas (modais e aviso rápido)
document.addEventListener('click', function (e) {
  // Abrir: <button data-abrir-modal="id-do-modal">
  var abrir = e.target.closest('[data-abrir-modal]');
  if (abrir) { openModal(abrir.dataset.abrirModal); return; }

  var closer = e.target.closest('[data-close-modal]');
  if (closer) { closer.closest('.modal').classList.remove('is-open'); return; }
  if (e.target.classList.contains('modal')) e.target.classList.remove('is-open');
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') document.querySelectorAll('.modal.is-open').forEach(function (m) { m.classList.remove('is-open'); });
});

function openModal(id) { document.getElementById(id).classList.add('is-open'); }
function closeModal(id) { document.getElementById(id).classList.remove('is-open'); }

function toast(msg) {
  var t = document.createElement('div');
  t.className = 'toast';
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(function () { t.classList.add('is-show'); }, 10);
  setTimeout(function () { t.classList.remove('is-show'); setTimeout(function () { t.remove(); }, 300); }, 2400);
}
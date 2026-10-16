// Painel do professor: só libera "Chamar" e "Marcar ausente" quando há alunos marcados
(function () {
  var checks = document.querySelectorAll('.sel');
  var chamar = document.getElementById('btn-chamar');
  var ausente = document.getElementById('btn-ausente');
  if (!chamar) return;

  function atualizar() {
    var algum = Array.prototype.some.call(checks, function (c) { return c.checked; });
    chamar.disabled = !algum;
    ausente.disabled = !algum;
  }
  checks.forEach(function (c) { c.addEventListener('change', atualizar); });
})();
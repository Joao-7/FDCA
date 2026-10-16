// Grade do aluno: abre o modal ao clicar numa célula e só libera o botão com texto digitado
(function () {
  var texto = document.getElementById('duvida-texto');
  var botao = document.getElementById('duvida-enviar');
  var aviso = document.getElementById('duvida-aviso');
  if (!texto) return;

  document.querySelectorAll('.cell[data-aula]').forEach(function (cell) {
    cell.addEventListener('click', function () {
      var ativo = cell.dataset.status === 'ativo' || cell.dataset.status === 'pausado';
      document.getElementById('duvida-aula').value = cell.dataset.aula;
      document.getElementById('duvida-disciplina').textContent = cell.dataset.disc;
      aviso.classList.toggle('is-hidden', ativo);
      botao.textContent = ativo ? 'Entrar na fila' : 'Enviar dúvida';
      texto.value = '';
      botao.disabled = true;
      openModal('modal-duvida');
      texto.focus();
    });
  });
  texto.addEventListener('input', function () { botao.disabled = !texto.value.trim(); });
})();
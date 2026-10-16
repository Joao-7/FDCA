// Grade do professor: ao clicar no lápis, preenche o modal com os dados da célula e o abre
document.querySelectorAll('.cell__edit').forEach(function (btn) {
  btn.addEventListener('click', function () {
    document.getElementById('ca-aula').value = btn.dataset.aula;
    document.getElementById('ca-sub').textContent = btn.dataset.disc + ' · ' + btn.dataset.turma;
    document.getElementById('ca-dia').value = btn.dataset.dia;
    document.getElementById('ca-inicio').value = btn.dataset.ini;
    document.getElementById('ca-fim').value = btn.dataset.fim;
    document.getElementById('ca-sem').checked = false;
    openModal('modal-ca');
  });
});
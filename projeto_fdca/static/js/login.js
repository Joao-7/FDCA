function selecionarPerfil(perfil, botao) {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    botao.classList.add('active');
    document.getElementById('perfil').value = perfil;

    const label = document.getElementById('label-identificador');
    const input = document.getElementById('identificador');

    if (perfil === 'professor') {
        label.textContent = 'E-mail institucional';
        input.placeholder = 'Ex: professor@ifrn.edu.br';
    } else {
        label.textContent = 'Matrícula ou e-mail';
        input.placeholder = 'Ex: 20241164010000';
    }
}
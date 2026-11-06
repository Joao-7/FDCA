from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CadastroForm, LoginForm
from .models import Perfil

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.usuario)
        if form.perfil.tipo == Perfil.TIPO_PROFESSOR:
            return redirect("grade_professor")
        return redirect("grade_aluno")

    # o template mostra a variável "erro" na caixa vermelha
    erro = next(iter(form.non_field_errors()), None) if request.method == "POST" else None
    return render(request, "conta/login.html", {"erro": erro})


def cadastro_view(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)  # formulário preenchido com o que foi enviado
        if form.is_valid():
            form.save()  # cria User + Perfil no banco
            return redirect("login")
    else:
        form = CadastroForm()  # primeira visita: formulário vazio

    # se chegou aqui, ou é GET ou o POST tinha erros (o form carrega os erros)
    return render(request, "conta/cadastro.html", {"form": form})
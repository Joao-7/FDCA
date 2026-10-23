from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import LoginForm
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
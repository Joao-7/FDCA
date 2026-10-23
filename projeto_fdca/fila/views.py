from django.shortcuts import render
from conta.decorators import perfil_requerido

@perfil_requerido("aluno") # Se não for aluno não entra nessa view
def grade_aluno(request):
    return render(request, "fila/grade_aluno.html")

@perfil_requerido("aluno")
def fila_aluno(request):
    return render(request, "fila/fila_aluno.html")

@perfil_requerido("professor")
def grade_professor(request):
    return render(request, "fila/grade_professor.html")


@perfil_requerido("professor")
def painel_professor(request):
    return render(request, "fila/painel_professor.html")


@perfil_requerido("professor")
def painel_professor_nao_iniciado(request):
    return render(request, "fila/painel_professor_nao_iniciado.html")


@perfil_requerido("professor")
def historico(request):
    return render(request, "fila/historico.html")


@perfil_requerido("professor")
def historico_detalhe(request):
    return render(request, "fila/historico_detalhe.html")
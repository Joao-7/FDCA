from django.shortcuts import render, redirect

def grade_aluno(request):
    return render(request, "fila/grade_aluno.html")

def fila_aluno(request):
    return render(request, "fila/fila_aluno.html")

def grade_professor(request):
    return render(request, "fila/grade_professor.html")

def painel_professor(request):
    return render(request, "fila/painel_professor.html")

def painel_professor_nao_iniciado(request):
    return render(request, "fila/painel_professor_nao_iniciado.html")

def historico(request):
    return render(request, "fila/historico.html")

def historico_detalhe(request):
    return render(request, "fila/historico_detalhe.html")
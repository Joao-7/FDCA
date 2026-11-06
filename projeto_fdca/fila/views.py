from django.db import IntegrityError, transaction
from django.shortcuts import render, redirect
from django.utils import timezone

from conta.decorators import perfil_requerido

from .forms import EntrarFilaForm
from .models import Atendimento, ItemFila


@perfil_requerido("aluno") # Se não for aluno não entra nessa view
def grade_aluno(request):
    return render(request, "fila/grade_aluno.html")

@perfil_requerido("aluno")
def fila_aluno(request):
    perfil = request.user.perfil_fdca  # ficha do aluno logado (related_name do model Perfil)

    # atendimento da turma do aluno que está ativo hoje (None se não houver)
    atendimento = Atendimento.objects.filter(
        turma=perfil.turma,
        data=timezone.localdate(),
        status=Atendimento.STATUS_ATIVO,
    ).first()

    # posição atual do aluno nessa fila, se ele já estiver nela
    meu_item = None
    if atendimento:
        meu_item = ItemFila.objects.filter(
            atendimento=atendimento,
            aluno=request.user,
            status__in=[ItemFila.STATUS_AGUARDANDO, ItemFila.STATUS_CHAMADO],
        ).first()

    if request.method == "POST":
        form = EntrarFilaForm(request.POST)  # formulário preenchido com o que foi enviado
        if form.is_valid():
            if atendimento is None:
                form.add_error(None, "Não há atendimento ativo para a sua turma agora.")
            else:
                item = form.save(commit=False)  # monta o ItemFila, mas ainda NÃO grava no banco
                item.atendimento = atendimento  # em qual fila o aluno está entrando
                item.aluno = request.user  # quem está entrando (o usuário logado)
                try:
                    with transaction.atomic():
                        item.save()  # agora sim grava
                except IntegrityError:
                    # o banco recusou: o aluno já tem um item ativo neste atendimento
                    form.add_error(None, "Você já está na fila deste atendimento.")
                else:
                    return redirect("fila_aluno")  # evita reenviar o formulário ao atualizar a página
    else:
        form = EntrarFilaForm()  # primeira visita: formulário vazio

    # se chegou aqui, ou é GET ou o POST tinha erros (o form carrega os erros)
    return render(request, "fila/fila_aluno.html", {
        "form": form,
        "atendimento": atendimento,
        "meu_item": meu_item,
    })

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
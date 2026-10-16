from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Atendimento(models.Model):
    """
    Sessão de Centro de Aprendizagem (C.A.) de uma turma.
    O professor controla o status (agendado, ativo, pausado, etc.).
    """
    STATUS_AGENDADO = 'agendado'
    STATUS_ATIVO = 'ativo'
    STATUS_PAUSADO = 'pausado'
    STATUS_ENCERRADO = 'encerrado'
    STATUS_CANCELADO = 'cancelado'
    STATUS_CHOICES = [
        (STATUS_AGENDADO, 'Agendado'),
        (STATUS_ATIVO, 'Ativo'),
        (STATUS_PAUSADO, 'Pausado'),
        (STATUS_ENCERRADO, 'Encerrado'),
        (STATUS_CANCELADO, 'Cancelado'),
    ]

    DIA_CHOICES = [
        (0, 'Segunda-feira'),
        (1, 'Terça-feira'),
        (2, 'Quarta-feira'),
        (3, 'Quinta-feira'),
        (4, 'Sexta-feira'),
    ]

    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='atendimentos_fdca'
    )
    disciplina = models.CharField(max_length=120)
    turma = models.CharField(max_length=30)
    dia = models.PositiveSmallIntegerField(choices=DIA_CHOICES)
    inicio = models.TimeField()
    fim = models.TimeField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_AGENDADO)
    data_excecao = models.DateField(blank=True, null=True)  # para cancelar um dia específico
    resumo = models.TextField(blank=True)
    comentario = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    encerrado_em = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['dia', 'inicio']

    def __str__(self):
        return f'{self.disciplina} - {self.turma} ({self.get_dia_display()})'


class ItemFila(models.Model):
    """
    Um aluno na fila de um atendimento.
    A ordem é pela data de criação (FIFO - quem chegou primeiro).
    """
    STATUS_AGUARDANDO = 'aguardando'
    STATUS_CHAMADO = 'chamado'
    STATUS_ATENDIDO = 'atendido'
    STATUS_AUSENTE = 'ausente'
    STATUS_DESISTIU = 'desistiu'
    STATUS_CHOICES = [
        (STATUS_AGUARDANDO, 'Aguardando'),
        (STATUS_CHAMADO, 'Chamado'),
        (STATUS_ATENDIDO, 'Atendido'),
        (STATUS_AUSENTE, 'Ausente'),
        (STATUS_DESISTIU, 'Desistiu'),
    ]

    atendimento = models.ForeignKey(
        Atendimento,
        on_delete=models.CASCADE,
        related_name='itens'
    )
    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='itens_fila_fdca'
    )
    duvida = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_AGUARDANDO)
    criado_em = models.DateTimeField(default=timezone.now)
    chamado_em = models.DateTimeField(blank=True, null=True)
    comentario = models.TextField(blank=True)

    class Meta:
        ordering = ['criado_em', 'id']
        constraints = [
            models.UniqueConstraint(
                fields=['atendimento', 'aluno'],
                condition=Q(status__in=['aguardando', 'chamado']),
                name='fdca_aluno_unico_na_fila_ativa'
            )
        ]

    def __str__(self):
        return f'{self.aluno} na fila de {self.atendimento}'
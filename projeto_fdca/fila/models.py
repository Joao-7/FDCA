from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Atendimento(models.Model):
    """Sessão de C.A. de uma turma, em uma data."""
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

    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='atendimentos_fdca',
    )
    turma = models.ForeignKey(
        'conta.Turma',
        on_delete=models.PROTECT,
        related_name='atendimentos',
    )
    disciplina = models.CharField(max_length=120)
    data = models.DateField()
    inicio = models.TimeField()
    fim = models.TimeField()
    vagas = models.PositiveSmallIntegerField(default=10)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_AGENDADO)
    resumo = models.TextField(blank=True)
    comentario = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    encerrado_em = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['data', 'inicio']
        constraints = [
            models.UniqueConstraint(
                fields=['turma', 'data', 'inicio'],
                name='fdca_horario_unico_por_turma',
            )
        ]

    def __str__(self):
        return f'{self.disciplina} - {self.turma} ({self.data:%d/%m/%Y})'


class ItemFila(models.Model):
    """Um aluno na fila de um atendimento. Ordem por chegada (FIFO)."""
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
        related_name='itens',
    )
    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='itens_fila_fdca',
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
                name='fdca_aluno_unico_na_fila_ativa',
            )
        ]

    def __str__(self):
        return f'{self.aluno} na fila de {self.atendimento}'
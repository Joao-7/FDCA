from django.conf import settings
from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=30, unique=True)  # ex.: INFO-3M

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Perfil(models.Model):
    TIPO_ALUNO = 'aluno'
    TIPO_PROFESSOR = 'professor'
    TIPO_CHOICES = [
        (TIPO_ALUNO, 'Aluno'),
        (TIPO_PROFESSOR, 'Professor'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_fdca',
    )
    matricula = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES)
    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alunos',
    )

    def __str__(self):
        nome = self.usuario.get_full_name() or self.usuario.username
        return f'{nome} ({self.get_tipo_display()})'
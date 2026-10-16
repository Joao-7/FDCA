from django.conf import settings
from django.db import models


class Perfil(models.Model):
    """
    Perfil extra do usuário do sistema FDCA.
    Liga o User do Django ao tipo (aluno ou professor) e à turma.
    """
    TIPO_ALUNO = 'aluno'
    TIPO_PROFESSOR = 'professor'
    TIPO_CHOICES = [
        (TIPO_ALUNO, 'Aluno'),
        (TIPO_PROFESSOR, 'Professor'),
    ]

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_fdca'
    )
    matricula = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=12, choices=TIPO_CHOICES)
    turma = models.CharField(max_length=30, blank=True)  # turma do aluno (texto simples por enquanto)

    def __str__(self):
        return f'{self.usuario.get_full_name() or self.usuario.username} ({self.get_tipo_display()})'
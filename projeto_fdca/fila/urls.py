from django.urls import path
from . import views


urlpatterns = [
    path("grade-aluno/", views.grade_aluno, name="grade_aluno"),
    path("fila-aluno/", views.fila_aluno, name="fila_aluno"),
    path("grade-professor/", views.grade_professor, name="grade_professor"),
    path("painel/", views.painel_professor, name="painel_professor"),
    path("painel-novo/", views.painel_professor_nao_iniciado, name="painel_professor_nao_iniciado"),
    path("historico/", views.historico, name="historico"),
    path("historico/detalhe/", views.historico_detalhe, name="historico_detalhe"),
]


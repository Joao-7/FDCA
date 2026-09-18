from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('/painel_aluno', views.painel_aluno, name='painel_aluno'),
]

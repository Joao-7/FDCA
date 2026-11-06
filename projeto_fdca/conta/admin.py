from django.contrib import admin
from .models import Perfil, Turma

admin.site.register(Turma)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'matricula', 'tipo', 'turma')
    list_editable = ('turma',)
    list_filter = ('tipo', 'turma')
    search_fields = ('matricula', 'usuario__username', 'usuario__first_name')
from django.contrib import admin

from .models import Atendimento, ItemFila

admin.site.register(Atendimento)
admin.site.register(ItemFila)
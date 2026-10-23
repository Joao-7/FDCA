from django import forms
from django.contrib.auth import authenticate

from .models import Perfil


class LoginForm(forms.Form):
    matricula = forms.CharField(max_length=30)
    senha = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        dados = super().clean()
        matricula = dados.get("matricula", "").strip()
        senha = dados.get("senha")
        if not matricula or not senha:
            return dados

        # 1. acha a ficha (Perfil) pela matrícula
        perfil = Perfil.objects.select_related("usuario").filter(matricula=matricula).first()

        # 2. confere a senha do usuário ligado a essa ficha
        usuario = None
        if perfil:
            usuario = authenticate(username=perfil.usuario.username, password=senha)

        if usuario is None:
            raise forms.ValidationError("Matrícula ou senha inválidas.")

        # guarda para a view usar (login e redirecionamento)
        self.usuario = usuario
        self.perfil = perfil
        return dados
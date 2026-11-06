from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction

from .models import Perfil

# modelo de usuário configurado no projeto (o mesmo do AUTH_USER_MODEL usado em models.py)
User = get_user_model()


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


class CadastroForm(forms.Form):
    """Formulário da tela de criação de conta."""

    nome = forms.CharField(
        label="Nome",
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite seu nome completo",
            "autocomplete": "name",
            "autofocus": True,
        }),
    )
    email = forms.EmailField(  # EmailField valida o formato do e-mail
        label="E-mail",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Digite seu e-mail",
            "autocomplete": "email",
        }),
    )
    matricula = forms.CharField(
        label="Matrícula",
        max_length=30,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Digite sua matrícula",
            "autocomplete": "username",
        }),
    )
    tipo = forms.ChoiceField(
        label="Tipo de conta",
        choices=Perfil.TIPO_CHOICES,  # mesma lista do model: se mudar lá, muda aqui
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Crie uma senha",
            "autocomplete": "new-password",
        }),
    )
    confirmar_senha = forms.CharField(
        label="Confirmar senha",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Digite a senha novamente",
            "autocomplete": "new-password",
        }),
    )

    # --- validações de campo único (rodam automaticamente: clean_<campo>) ---

    def clean_matricula(self):
        matricula = self.cleaned_data["matricula"].strip()
        # a matrícula será o username, então precisa ser única nas duas tabelas
        if (
            Perfil.objects.filter(matricula=matricula).exists()
            or User.objects.filter(username=matricula).exists()
        ):
            raise ValidationError("Já existe uma conta com esta matrícula.")
        return matricula

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Já existe uma conta com este e-mail.")
        return email

    # --- validação que compara campos entre si ---

    def clean(self):
        dados = super().clean()
        senha = dados.get("senha")
        confirmar = dados.get("confirmar_senha")

        if senha:
            # usuário temporário (não é salvo) para o Django comparar a senha
            # com nome/e-mail/matrícula e recusar senhas parecidas com eles
            usuario_temp = User(
                username=dados.get("matricula", ""),
                email=dados.get("email", ""),
                first_name=dados.get("nome", ""),
            )
            try:
                validate_password(senha, user=usuario_temp)
            except ValidationError as erro:
                self.add_error("senha", erro)

        if senha and confirmar and senha != confirmar:
            self.add_error("confirmar_senha", "As senhas não coincidem.")

        return dados

    # --- gravação no banco ---

    def save(self):
        """Cria o User e o Perfil juntos. Chamar só depois de is_valid()."""
        dados = self.cleaned_data
        with transaction.atomic():
            usuario = User.objects.create_user(
                username=dados["matricula"],
                email=dados["email"],
                password=dados["senha"],  # create_user criptografa a senha
                first_name=dados["nome"],
            )
            Perfil.objects.create(
                usuario=usuario,
                matricula=dados["matricula"],
                tipo=dados["tipo"],
            )
        return usuario
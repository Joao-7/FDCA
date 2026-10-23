from django import forms
from .models import ItemFila


class EntrarFilaForm(forms.ModelForm):
    class Meta:
        model = ItemFila
        fields = ['duvida']
        widgets = {
            'duvida': forms.Textarea(attrs={
                'placeholder': 'Ex: Tenho dúvida sobre como aplicar o padrão MVC na camada de serviço...',
                'rows': 4,
                'class': 'input',
            }),
        }
        labels = {
            'duvida': 'Qual é a sua dúvida?',
        }

    def clean_duvida(self):
        duvida = self.cleaned_data.get('duvida', '').strip()
        if len(duvida) > 500:
            raise forms.ValidationError("A dúvida deve ter no máximo 500 caracteres.")
        return duvida
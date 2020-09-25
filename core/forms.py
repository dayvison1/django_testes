from django import forms

from .models import Vagas


class VagasModelForms(forms.ModelForm):

    class Meta:
        model=Vagas
        fields = ('nomeCliente', 'telefoneCliente', 'servicoCliente')
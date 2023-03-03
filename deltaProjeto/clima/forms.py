from django.forms import ModelForm

from django import forms
from .models import Localizacao

class LocalizacaoForm(forms.ModelForm):
    class Meta:
        model = Localizacao
        fields = ['estado', 'cidade']
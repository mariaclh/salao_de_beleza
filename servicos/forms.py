from django import forms
from .models import Servico, ProfissionalServico
from datetime import date

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['descricao']
        
class ProfissionalServicoForm(forms.ModelForm):
    class Meta:
        model = ProfissionalServico
        fields = ['profissional', 'servico', 'valor']
        # widgets = {
        #    'profissional': forms.Select(attrs={'class': 'form-control'}),
        #    'servico': forms.Select(attrs={'class': 'form-control'}),
        #    'valor': forms.NumberInput(attrs={'class': 'form-control'}),
        # }
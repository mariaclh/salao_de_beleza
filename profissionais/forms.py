from django import forms
from .models import Profissional
from datetime import date

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['nome', 'cpf', 'data_nascimento', 'telefone', 'email']
        
        widgets = {
            'data_nascimento': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'max': date.today().isoformat(),
                    }
                
            ),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        
        if Profissional.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Já existe um profissional cadastrado com este CPF.")
            
        return cpf
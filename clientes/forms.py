from django import forms
from .models import Cliente
from datetime import date

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
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
        
        if Cliente.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError("Já existe um cliente cadastrado com este CPF.")
            
        return cpf
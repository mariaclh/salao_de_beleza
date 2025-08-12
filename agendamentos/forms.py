from django import forms
from django.core.exceptions import ValidationError
from datetime import date, time
from .models import Agendamento
from django.db.models import Q

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['cliente', 'profissional_servico', 'data', 'hora_inicio', 'hora_fim', 'status']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        data = cleaned_data.get('data')
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fim = cleaned_data.get('hora_fim')
        profissional_servico = cleaned_data.get('profissional_servico')


        if data and data < date.today():
            raise ValidationError("A data do agendamento não pode ser anterior à data de hoje.")

        if hora_inicio and hora_fim:
            if hora_fim <= hora_inicio:
                raise ValidationError("A hora de fim deve ser posterior à hora de início.")

        profissional = profissional_servico.profissional

        conflitos = Agendamento.objects.filter(
            profissional_servico__profissional=profissional,
            data=data
        ).exclude(
            status='cancelado'
        ).filter(
            Q(hora_fim__gt=hora_inicio) & Q(hora_inicio__lt=hora_fim)
        )
        
        if self.instance.pk:
            conflitos = conflitos.exclude(pk=self.instance.pk)

        if conflitos.exists():
            raise ValidationError(
                "O profissional já possui um agendamento neste horário."
            )

        
        return cleaned_data
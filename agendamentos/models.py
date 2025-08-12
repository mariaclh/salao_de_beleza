from django.db import models
from clientes.models import Cliente  
from servicos.models import ProfissionalServico 

STATUS_CHOICES = (
    ('agendado', 'Agendado'),
    ('concluido', 'Concluído'),
    ('cancelado', 'Cancelado'),
)

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='agendamentos_cliente', verbose_name='Cliente')
    profissional_servico = models.ForeignKey(ProfissionalServico, on_delete=models.CASCADE, related_name='agendamentos_profissional_servico', verbose_name='Serviço')

    data = models.DateField(verbose_name='Data do agendamento')
    hora_inicio = models.TimeField(verbose_name='Hora de início')
    hora_fim = models.TimeField(null=True, blank=True, verbose_name='Hora de fim')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='agendado',
        verbose_name='Status',
    )
    
    def __str__(self):
        return f'Agendamento de {self.cliente} com {self.profissional_servico} em {self.data}'
        
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = ['data', 'hora_inicio'] # Ordena por data e hora no admin
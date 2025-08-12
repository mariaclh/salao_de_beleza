from django.db import models
from profissionais.models import Profissional

class Servico(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição de serviço')

    def __str__(self):
        return self.descricao

class ProfissionalServico(models.Model):
    
    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        related_name='servicos_oferecidos',
        verbose_name='Profissional', 
    )
    
    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        related_name='profissionais_do_servico',
        verbose_name='Serviço',
    )
    
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name='Valor',
    )

    def __str__(self):
        return f'{self.profissional.nome} - {self.servico.descricao} - R$ {self.valor}'
        
    class Meta:
        verbose_name = 'Serviço de Profissional'
        verbose_name_plural = 'Serviços de Profissionais'
        unique_together = ('profissional', 'servico')
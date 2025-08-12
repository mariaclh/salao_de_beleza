from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(unique=True, verbose_name='E-mail')

    def __str__(self):
        return self.nome
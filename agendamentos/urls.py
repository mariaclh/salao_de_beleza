from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_agendamento, name='criar_agendamento'),
    path('gerenciar/', views.gerenciar_agendamentos, name='gerenciar_agendamentos'),
    path('relatorio/concluidos/', views.gerar_relatorio, name='gerar_relatorio'),
]
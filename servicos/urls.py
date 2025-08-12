from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.cadastrar_servico, name='cadastrar_servico'),
    path('associar/', views.criar_profissional_servico, name='criar_profissional_servico'),
]
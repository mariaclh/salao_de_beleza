from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_profissional, name='cadastrar_profissional'),
]
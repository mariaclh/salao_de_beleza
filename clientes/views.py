from django.shortcuts import render, redirect
from django.contrib import messages # Framework de mensagens
from .forms import ClienteForm

def cadastrar_cliente(request):
    # Requisição do tipo POST, formulário foi submetido.
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        # Algumas validações do forms.py
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('cadastrar_cliente') # Redireciona para a mesma página limpando o formulário
    
    # Exibe o formulário vazio.
    else:
        form = ClienteForm()
        
    return render(request, 'clientes/cadastro_cliente.html', {'form': form})
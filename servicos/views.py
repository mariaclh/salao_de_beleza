from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import ServicoForm, ProfissionalServicoForm

def cadastrar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de serviço cadastrado com sucesso!")
            return redirect('cadastrar_servico') 
    else:
        form = ServicoForm()
        
    return render(request, 'servicos/cadastro_servico.html', {'form': form})

def criar_profissional_servico(request):
    if request.method == 'POST':
        form = ProfissionalServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Serviço cadastrado com sucesso!")
            return redirect('criar_profissional_servico') 
    else:
        form = ProfissionalServicoForm()

    return render(request, 'servicos/criar_profissional_servico.html', {'form': form})
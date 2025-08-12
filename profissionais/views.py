from django.shortcuts import render, redirect
from django.contrib import messages  
from .forms import ProfissionalForm

def cadastrar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Profissional cadastrado com sucesso!")
            return redirect('cadastrar_profissional') 
    else:
        form = ProfissionalForm()
        
    return render(request, 'profissionais/cadastro_profissional.html', {'form': form})
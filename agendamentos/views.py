from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib import messages
from datetime import datetime

def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Agendado com sucesso!")
            return redirect('criar_agendamento') 
    else:
        form = AgendamentoForm()
        
    return render(request, 'agendamentos/criar_agendamento.html', {'form': form})


def gerenciar_agendamentos(request):
    data_filtrada = request.GET.get('data')

    if data_filtrada:
        try:
            data_filtrada_obj = datetime.strptime(data_filtrada, '%Y-%m-%d').date()
        except ValueError:
            data_filtrada_obj = timezone.localdate()
    else:
        data_filtrada_obj = timezone.localdate()

    agendamentos = Agendamento.objects.filter(data=data_filtrada_obj).order_by('hora_inicio')

    if request.method == 'POST':
        agendamento_id = request.POST.get('agendamento_id')
        novo_status = request.POST.get('status')
        agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
        
        if novo_status in ['confirmado', 'cancelado', 'concluido']: 
            agendamento.status = novo_status
            agendamento.save()
            messages.success(request, "Status do agendamento atualizado com sucesso!")
        else:
            messages.error(request, "Status inválido.")

        return redirect('gerenciar_agendamentos')

    context = {
        'agendamentos': agendamentos,
        'data_filtrada': data_filtrada_obj,
    }
    
    return render(request, 'agendamentos/gerenciar_agendamentos.html', context)

def gerar_relatorio(request):
    data_inicio_str = request.GET.get('data_inicio')
    data_fim_str = request.GET.get('data_fim')
    agendamentos_count = None

    if data_inicio_str and data_fim_str:
        try:
            data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d').date()
            data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d').date()

            agendamentos = Agendamento.objects.filter(
                data__range=[data_inicio, data_fim],
                status='concluido' 
            )
            agendamentos_count = agendamentos.count()
            messages.success(request, f"Relatório de agendamentos concluídos gerado com sucesso para o período de {data_inicio_str} a {data_fim_str}.")

        except ValueError:
            messages.error(request, "Formato de data inválido. Por favor, use YYYY-MM-DD.")

    context = {
        'agendamentos_count': agendamentos_count,
        'data_inicio': data_inicio_str,
        'data_fim': data_fim_str,
    }

    return render(request, 'agendamentos/relatorio_agendamentos.html', context)

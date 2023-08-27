from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from cadastro.models import cadastro_produto
from django.http import JsonResponse
from .models import Cronometro

# Create your views here.
@login_required
def monitoramento(request):
    if request.method == "GET":
        return render(request, 'monitoramento/monitoramento.html')


def logout(request):
    user = auth.logout(request)
    return redirect('login/')


@login_required
def maquina(request):
    if request.method == "GET":
        return render(request, 'monitoramento/maquina.html')
    
    if request.method == "POST":
        numero_da_of = request.POST.get('of6numeros')
        codigo_produto = request.POST.get('codigoproduto')
        quantidade_of = request.POST.get('quantidadeof')
        cadastros = cadastro_produto.objects.filter(codigo_produto=codigo_produto)                  
        return render(request, 'monitoramento/maquina.html', {'cadastros': cadastros, 
                                                               'numero_da_of': numero_da_of, 
                                                               'quantidade_of': quantidade_of,
                                                                })    

   
@login_required
def get_timer_state(request):
    cronometro = Cronometro.objects.first()

    if cronometro is not None:
        is_running = cronometro.is_running
        seconds = cronometro.seconds
    else:
        is_running = False
        seconds = 0

    data = {
        'is_running': is_running,
        'seconds': seconds
    }

    return JsonResponse(data)
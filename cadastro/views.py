from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import cadastro_produto
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
@login_required
def cadastrar_produto(request):
    if request.method == "GET":
        codigo = request.GET.get('filtro_produto')        
        cadastros = cadastro_produto.objects.all()
        if codigo:
            cadastros = cadastros.filter(codigo_produto=codigo)
        return render(request, 'cadastro/cadastrar_produto.html', {'cadastros': cadastros})        
    elif request.method == "POST":        
        codigo_produto = request.POST.get('codigo_produto')
        produto = request.POST.get('produto')
        tempo_produto = request.POST.get('tempo_produto')

        cadastro = cadastro_produto(
            criador = request.user,            
            codigo_produto = codigo_produto,
            produto = produto,
            tempo_produto = tempo_produto,
        )

        cadastro.save()

        messages.add_message(request, constants.SUCCESS, 'Produto cadastrado com sucesso.')
        return redirect(reverse('cadastrar_produto'))


@login_required
def editar_produto(request, id):
    codigo = cadastro_produto.objects.get(id=id)
    return render(request, "cadastro/editar_produto.html", {"codigo": codigo})


@login_required
def update(request, id):    
    codigo_produto = request.POST.get("codigo_produto") 
    produto = request.POST.get("produto") 
    tempo_produto = request.POST.get("tempo_produto") 
    codigo = cadastro_produto.objects.get(id=id)              
    codigo.codigo_produto = codigo_produto
    codigo.produto = produto
    codigo.tempo_produto = tempo_produto     
    codigo.save()
    return redirect(reverse('produtos_cadastrados'))


@login_required
def delete(request, id):
    codigo = cadastro_produto.objects.get(id=id)
    codigo.delete()
    return redirect(reverse('produtos_cadastrados'))
       

@login_required
def produtos_cadastrados(request):
    if request.method == "GET":
        codigo = request.GET.get('filtro_produto')        
        cadastros = cadastro_produto.objects.all()
        if codigo:
            cadastros = cadastros.filter(codigo_produto=codigo)
        return render(request, 'cadastro/produtos_cadastrados.html', {'cadastros': cadastros})        
    




    




from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth


# Create your views here.

#A classe LoginView "extends" TemplateView
def login(request):            
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)    

        if not user:
            messages.add_message(request, constants.ERROR, 'Nome do usuário ou senha inválidos')
            return redirect(reverse('login'))
            
        auth.login(request, user)
        return redirect('/monitoramento/')
    

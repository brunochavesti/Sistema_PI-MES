from django.urls import path
from usuarios import views

# Importar as views que foram criadas em usuarios/urls.py

urlpatterns = [
    #path('caminho_da_url/', MinhaView.asview(), name='nome-da-url'),
    path('login/', views.login, name="login"),
       
]
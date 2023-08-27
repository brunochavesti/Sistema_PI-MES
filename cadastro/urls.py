from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),    
    path('produtos_cadastrados/', views.produtos_cadastrados, name='produtos_cadastrados'),
    path('produtos_cadastrados/editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('produtos_cadastrados/update/<int:id>', views.update, name='update'),
    path('produtos_cadastrados/delete/<int:id>', views.delete, name='delete'),
]
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cadastro_produto(models.Model):
    criador = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)    
    codigo_produto = models.CharField(max_length=5)
    produto = models.TextField()
    tempo_produto = models.IntegerField()

    def __str__(self) -> str:
        return self.codigo_produto
    

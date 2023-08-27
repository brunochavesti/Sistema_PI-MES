from django.db import models

# Create your models here.
class Cronometro(models.Model):
    is_running = models.BooleanField(default=False)
    seconds = models.IntegerField(default=0)
    
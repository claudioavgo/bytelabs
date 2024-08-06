from django.db import models

# Create your models here.

class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
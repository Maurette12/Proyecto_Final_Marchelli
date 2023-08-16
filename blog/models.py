from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    fecha = models.DateField(null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lista_articulos")

    def __str__(self):
        return f"{self.titulo}, {self.autor}"
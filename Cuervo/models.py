from django.db import models

# Create your models here.
class Futbolista(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    posicion = models.CharField(max_length=256)
    altura = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"


class Socio(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    socio_n = models.IntegerField(null=True) 

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.socio_n}"

class Autoridad(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    cargo = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.cargo}"


class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=256)
    autor = models.CharField(max_length=256)
    fecha = models.DateField(null=True)

    def __str__(self):
        return f"{self.titulo}, {self.autor}"
    
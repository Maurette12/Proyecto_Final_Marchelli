from django.contrib import admin

from Cuervo.models import Futbolista, Socio, Autoridad, Articulo

# Register your models here.
admin.site.register(Futbolista)
admin.site.register(Socio)
admin.site.register(Autoridad)
admin.site.register(Articulo)
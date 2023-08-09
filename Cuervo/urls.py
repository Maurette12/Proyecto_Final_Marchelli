from django.contrib import admin
from django.urls import path

from Cuervo.views import listar_futbolistas, listar_autoridades


# Son las URLS especificas de la app
urlpatterns = [
    path("futbolistas/", listar_futbolistas, name="lista_futbolistas"),
    path("autoridades/", listar_autoridades, name="lista_autoridades")
]
from django.contrib import admin
from django.urls import path

from Cuervo.views import listar_futbolistas


# Son las URLS especificas de la app
urlpatterns = [
    path("matadores/", listar_futbolistas),
]

from django.urls import path

from blog.views import crear_articulo, listar_articulos


urlpatterns = [
    path("crear-articulo/", crear_articulo, name="crear_articulo"),
    path("lista-articulos/", listar_articulos, name="lista_articulos")
]
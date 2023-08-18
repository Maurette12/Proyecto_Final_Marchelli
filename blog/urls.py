
from django.urls import path

from blog.views import crear_articulo, listar_articulos, eliminar_articulo, editar_articulo, detalle_articulo
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("crear-articulo/", crear_articulo, name="crear_articulo"),
    path("lista-articulos/", listar_articulos, name="lista_articulos"),
    path("eliminar-articulo/<int:id>/", eliminar_articulo, name="eliminar_articulo"),
    path("editar-articulo/<int:id>/", editar_articulo, name="editar_articulo"),
    path('<int:articulo_id>/', detalle_articulo, name='detalle_articulo')
]
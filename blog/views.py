from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from blog.forms import ArticuloFormulario
from blog.models import Articulo

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def listar_articulos(request):
    contexto = {
        "articulos": Articulo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name="blog/lista_articulos.html",
        context=contexto,
    )
    return http_response


# Create your views here.
@login_required
def crear_articulo(request):
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            titulo = data["titulo"]
            subtitulo = data["subtitulo"]
            cuerpo = data["cuerpo"]
            autor = data["autor"]
            fecha = data["fecha"]
            articulo = Articulo(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha)
            articulo.save()

            
            url_exitosa = reverse('lista_articulos') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = ArticuloFormulario()
    http_response = render(
        request=request,
        template_name='blog/formulario_articulo.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def eliminar_articulo(request, id):
    # obtienes el curso de la base de datos
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        articulo.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse("lista_articulos")
        return redirect(url_exitosa)

@login_required
def editar_articulo(request, id):
    articulo = Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario = ArticuloFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            articulo.titulo = data['titulo']
            articulo.subtitulo = data['titulo']
            articulo.cuerpo = data['cuerpo']
            articulo.autor = data['autor']
            articulo.fecha = data['fecha']
            articulo.save()

            url_exitosa = reverse('lista_articulos')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': articulo.titulo,
            'subtitulo': articulo.subtitulo,
            'cuerpo': articulo.cuerpo,
            'autor': articulo.autor,
            'fecha': articulo.fecha,
        }
        formulario = ArticuloFormulario(initial=inicial)
    return render(
        request=request,
        template_name='blog/formulario_articulo.html',
        context={'formulario': formulario},
    )
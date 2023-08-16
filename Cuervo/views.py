from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from Cuervo.models import Futbolista, Socio, Autoridad

# Create your views here.
def listar_futbolistas(request):
    contexto = {
        "futbolistas": Futbolista.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Cuervo/lista_futbolistas.html',
        context=contexto,
    )
    return http_response


def listar_autoridades(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "autoridades": Autoridad.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Cuervo/lista_autoridades.html',
        context=contexto,
    )
    return http_response


def listar_socios(request):
    contexto = {
        "socios": Socio.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Cuervo/lista_socios.html',
        context=contexto,
    )
    return http_response


def acerca_de_mi(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='Cuervo/acerca_de_mi.html',
        context=contexto,
    )
    return http_response
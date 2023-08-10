from django.shortcuts import render

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
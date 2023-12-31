from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse



def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_html(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name="templates/base.html",
        context=contexto,
    )
    return http_response


def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='templates/inicio.html',
        context=contexto,
    )
    return http_response
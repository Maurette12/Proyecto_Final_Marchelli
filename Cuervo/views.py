from django.shortcuts import render

# Create your views here.
def listar_futbolistas(request):
    contexto = {
        "futbolistas": [
            {"nombre": "Augusto", "apellido": "Batalla"},
            {"nombre": "Nahuel", "apellido": "Barrios"},
            {"nombre": "Adam", "apellido": "Bareiro"},
            {"nombre": "Ivan", "apellido": "Leguizamon"},
        ]
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
        "autoridades": [
            {"nombre": "Carlos Horacio Arreceygor", "cargo": "Presidente"},
            {"nombre": "Miguel Marcelo Mastrosimone", "cargo": "Vicepresidente"},
            {"nombre": "Sergio Gabriel Costantino", "cargo": "Secretario"},
        ]
    }
    http_response = render(
        request=request,
        template_name='Cuervo/lista_autoridades.html',
        context=contexto,
    )
    return http_response
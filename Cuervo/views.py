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

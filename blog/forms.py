from django import forms


class ArticuloFormulario(forms.Form):
    titulo = forms.CharField(required=True, max_length=64)
    subtitulo = forms.CharField(required=True, max_length=256)
    cuerpo = forms.CharField(required=True, max_length=2048)
    autor = forms.CharField(required=True, max_length=256)
    fecha = forms.DateField(required=True)
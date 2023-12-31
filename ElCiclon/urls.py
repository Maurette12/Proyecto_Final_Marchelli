"""
URL configuration for ElCiclon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ElCiclon.views import saludar_con_fecha, saludar_con_html, inicio

urlpatterns = [
    path("", inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path("control/", include("Cuervo.urls")),
    path("blog/", include("blog.urls")),
    path("perfiles/", include("perfiles.urls")),
    #secundarias
    path("saludo-hoy/", saludar_con_fecha),
    path("saludo-html/", saludar_con_html),
]

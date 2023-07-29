from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('autos', autos, name="autos"),
    path('motos', motos, name="motos"),
    path('empleados', empleados, name="empleados"),
    path('clientes', clientes, name="clientes"),

    path('autos_form', autosForm, name="autos_form"),
    path('motos_form', motosForm, name="motos_form"),
    path('empleados_form', empleadosForm, name="empleados_form"),
    path('clientes_form', clientesForm, name="clientes_form"),

    path('buscar_autos', buscarAuto, name="buscar_autos"),
    path('buscarAuto2', buscarAuto2, name="buscarAuto2"),

    path('buscar_motos', buscarMoto, name="buscar_motos"),
    path('buscarMoto2', buscarMoto2, name="buscarMoto2"),
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'aplicacion/base.html')

def autos(request):
    ctx = {"autos": Auto.objects.all()}
    return render(request, 'aplicacion/autos.html', ctx)

def motos(request):
    ctx = {"motos": Moto.objects.all()}
    return render(request, 'aplicacion/motos.html', ctx)

def empleados(request):
    ctx = {"empleados": Empleado.objects.all()}
    return render(request, 'aplicacion/empleados.html', ctx)

def clientes(request):
    ctx = {"clientes": Cliente.objects.all()}
    return render(request, 'aplicacion/clientes.html', ctx)

def autosForm(request):
    if request.method == "POST":
        miForm = AutoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            auto = Auto(marca=informacion['marca'], modelo=informacion['modelo'], anio=informacion['anio'], kilometraje=informacion['kilometraje'])
            auto.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = AutoForm()      
    
    return render(request, "aplicacion/autosForm.html", {"form":miForm})


def motosForm(request):
    if request.method == "POST":
        miForm = MotoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            moto = Moto(marca=informacion['marca'], modelo=informacion['modelo'], anio=informacion['anio'], kilometraje=informacion['kilometraje'])
            moto.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = MotoForm()      
    
    return render(request, "aplicacion/motosForm.html", {"form":miForm})

def empleadosForm(request):
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            empleado = Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
            empleado.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = EmpleadoForm()      
    
    return render(request, "aplicacion/empleadosForm.html", {"form":miForm})

def clientesForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
            cliente.save()
            return render(request, "aplicacion/base.html")  
    else:
        miForm = ClienteForm()      
    
    return render(request, "aplicacion/clientesForm.html", {"form":miForm})

def buscarAuto(request):
    return render(request, "aplicacion/buscarAuto.html")

def buscarAuto2(request):
    if request.GET['marca']:
        marca = request.GET['marca']
        autos = Auto.objects.filter(marca__icontains=marca)
        return render(request, 
                      "aplicacion/resultadoBuscarAuto.html",
                      {"marca": marca, "autos":autos})
    
def buscarMoto(request):
    return render(request, "aplicacion/buscarMoto.html")

def buscarMoto2(request):
    if request.GET['marca']:
        marca = request.GET['marca']
        motos = Moto.objects.filter(marca__icontains=marca)
        return render(request, 
                      "aplicacion/resultadoBuscarMoto.html",
                      {"marca": marca, "motos":motos})
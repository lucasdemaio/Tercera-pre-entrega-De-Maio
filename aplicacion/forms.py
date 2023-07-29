from django import forms

class AutoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    anio = forms.IntegerField(label="Año", required=True)
    kilometraje = forms.IntegerField(label="Kilometraje", required=True)

class MotoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=50, required=True)
    modelo = forms.CharField(label="Modelo", max_length=50, required=True)
    anio = forms.IntegerField(label="Año", required=True)
    kilometraje = forms.IntegerField(label="Kilometraje", required=True)

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.IntegerField(label="Telefono", required=True)
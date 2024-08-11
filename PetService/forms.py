from django import forms


class MascotaFormulario(forms.Form):
    nombre_mascota = forms.CharField()
    fecha_nacimiento = forms.DateField()
    edad = forms.CharField()
    sexo = forms.CharField()
    especie = forms.CharField()
    raza = forms.CharField()
    profesional_a_cargo = forms.CharField()
    propietario = forms.CharField()


class PropietarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    dni = forms.CharField()
    telefono = forms.CharField()
    email = forms.EmailField()
    direccion = forms.CharField()
    nombre_mascota = forms.CharField()


class VeterinarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    cargo = forms.CharField()

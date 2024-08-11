from django.db import models


# Create your models here.


class Propietario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50)
    nombre_mascota = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'


class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField(null=True, blank=True)
    sexo = models.CharField(max_length=6)
    especie = models.CharField(max_length=10)
    raza = models.CharField(max_length=50)
    profesional_a_cargo = models.ForeignKey(
        "Veterinario", on_delete=models.CASCADE, null=True, blank=True)
    propietario = models.ForeignKey(
        "Propietario", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre_mascota}, {self.raza}'


class Servicio(models.Model):
    desparasitacion = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    vacunacion = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    chequeo_sangre = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    servicio_peluqueria = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    alimento = models.CharField(max_length=100, blank=True, null=True)
    varios = models.CharField(max_length=150, default='', blank=True)
    mascota = models.ForeignKey("mascota", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.mascota}'


class Veterinario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cargo = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

from django.contrib import admin
from .models import Mascota, Propietario, Servicio, Veterinario

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre_mascota', 'especie', 'raza')
    list_per_page = 10
    list_filter = ('nombre_mascota',)
    ordering = ('nombre_mascota', 'raza')

class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'email')
    list_per_page = 10

class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo')

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Propietario, PropietarioAdmin)
admin.site.register(Servicio)
admin.site.register(Veterinario, VeterinarioAdmin)


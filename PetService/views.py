from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Propietario, Mascota, Servicio, Veterinario

# Create your views here.


def inicio(request):
    return render(request, 'PetService/inicio.html')


def mostrar_servicios(request):

    servicios = Servicio.objects.all()

    contexto = {'servicios': servicios}

    return render(request, 'PetService/servicios.html', contexto)


def about(request):
    return render(request, 'PetService/about.html')


def contact(request):
    return render(request, 'PetService/contact.html')

# clases para propietarios


class PropietarioListView(LoginRequiredMixin, ListView):
    model = Propietario
    context_object_name = 'propietario'
    template_name = 'PetService/propietario_list.html'


class PropietarioDetailView(LoginRequiredMixin, DetailView):
    model = Propietario
    template_name = 'PetService/propietario_detail.html'


class PropietarioCreateView(LoginRequiredMixin, CreateView):
    model = Propietario
    template_name = 'PetService/propietario_create.html'
    success_url = reverse_lazy('propietario_list')
    fields = ['nombre', 'apellido', 'dni',
              'telefono', 'email', 'direccion', 'nombre_mascota']


class PropietarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Propietario
    template_name = 'PetService/propietario_update.html'
    success_url = reverse_lazy('propietario_list')
    fields = ['nombre', 'apellido', 'dni',
              'telefono', 'email', 'direccion', 'nombre_mascota']


class PropietarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Propietario
    template_name = 'PetService/propietario_delete.html'
    success_url = reverse_lazy('propietario_list')

# clases para mascotas


class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    context_object_name = 'mascota'
    template_name = 'PetService/mascota_list.html'


class MascotaDetailView(LoginRequiredMixin, DetailView):
    model = Mascota
    template_name = 'PetService/mascota_detail.html'


class MascotaCreateView(LoginRequiredMixin, CreateView):
    model = Mascota
    template_name = 'PetService/mascota_create.html'
    success_url = reverse_lazy('mascota_list')
    fields = ['nombre_mascota', 'fecha_nacimiento', 'edad', 'sexo',
              'especie', 'raza', 'propietario']


class MascotaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mascota
    template_name = 'PetService/mascota_update.html'
    success_url = reverse_lazy('mascota_list')
    fields = ['nombre_mascota', 'fecha_nacimiento', 'edad', 'sexo',
              'especie', 'raza', 'profesional_a_cargo', 'propietario']


class MascotaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'PetService/mascota_delete.html'
    success_url = reverse_lazy('mascota_list')

# clases para veterinario


class VeterinarioListView(LoginRequiredMixin, ListView):
    model = Veterinario
    context_object_name = 'veterinario'
    template_name = 'PetService/veterinario_list.html'


class VeterinarioDetailView(LoginRequiredMixin, DetailView):
    model = Veterinario
    template_name = 'PetService/veterinario_detail.html'


class VeterinarioCreateView(LoginRequiredMixin, CreateView):
    model = Veterinario
    template_name = 'PetService/veterinario_create.html'
    success_url = reverse_lazy('veterinario_list')
    fields = ['nombre', 'apellido', 'cargo']


class VeterinarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Veterinario
    template_name = 'PetService/veterinario_update.html'
    success_url = reverse_lazy('veterinario_list')
    fields = ['nombre', 'apellido', 'cargo']


class VeterinarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Veterinario
    template_name = 'PetService/veterinario_delete.html'
    success_url = reverse_lazy('veterinario_list')



from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from usuarios.forms import UserRegisterForm, UserEditForm
from django.urls import reverse_lazy


# Create your views here.

# PabloB    --> user
# pabloerik15 --> password

def login_request(request):
    msg_login = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, 'PetService/inicio.html')
        msg_login = 'Usuario o contraseña incorrecta!'

    form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form, 'msg_login': msg_login})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'PetService/inicio.html', {'mensaje': 'Usuario creado con exito!'})
    else:
        form = UserRegisterForm()

    return render(request, 'usuarios/register.html', {'form': form})


@login_required
def edit_user(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(
            request.POST, request.FILES, instance=usuario)
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get(
                    'imagen')
                usuario.avatar.save()
            mi_formulario.save()
            return render(request, 'PetService/inicio.html')

    else:
        mi_formulario = UserEditForm(instance=request.user)

    return render(request, 'usuarios/edit_user.html', {'form': mi_formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/change_password.html'
    success_url = reverse_lazy('edit_user')

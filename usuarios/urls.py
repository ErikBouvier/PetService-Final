from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login_request, register, edit_user
from .views import CambiarContrasenia

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='PetService/inicio.html'), name='logout'),
    path('edit-user/', edit_user, name='edit_user'),
    path('change-password/', CambiarContrasenia.as_view(), name='change_password'),
]

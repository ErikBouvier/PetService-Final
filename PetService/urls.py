from django.urls import path

from PetService.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('servicios/', mostrar_servicios, name='servicios'),
    path('propietario-list/', PropietarioListView.as_view(),
         name='propietario_list'),
    path('propietario-detail/<pk>', PropietarioDetailView.as_view(),
         name='propietario_detail'),
    path('propietario-create/<int:id>',
         PropietarioCreateView.as_view(), name='propietario_create'),
    path('propietario-update/<pk>/edit',
         PropietarioUpdateView.as_view(), name='propietario_update'),
    path('propietario-delete/<pk>/delete',
         PropietarioDeleteView.as_view(), name='propietario_delete'),
]

mascotas = [
    path('mascota-list/', MascotaListView.as_view(), name='mascota_list'),
    path('mascota-detail/<pk>', MascotaDetailView.as_view(), name='mascota_detail'),
    path('mascota-create/<int:id>',
         MascotaCreateView.as_view(), name='mascota_create'),
    path('mascota-update/<pk>/edit',
         MascotaUpdateView.as_view(), name='mascota_update'),
    path('mascota-delete/<pk>/delete',
         MascotaDeleteView.as_view(), name='mascota_delete'),
]

urlpatterns += mascotas

veterinarios = [
    path('veterinario-list/', VeterinarioListView.as_view(),
         name='veterinario_list'),
    path('veterinario-detail/<pk>', VeterinarioDetailView.as_view(),
         name='veterinario_detail'),
    path('veterinario-create/<int:id>',
         VeterinarioCreateView.as_view(), name='veterinario_create'),
    path('veterinario-update/<pk>/edit',
         VeterinarioUpdateView.as_view(), name='veterinario_update'),
    path('veterinario-delete/<pk>/delete',
         VeterinarioDeleteView.as_view(), name='veterinario_delete'),
]

urlpatterns += veterinarios


info_petservice = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

urlpatterns += info_petservice

PETSERVICE

Descripción:
PetService es una aplicación web desarrollada con Python y Django que permite gestionar información sobre mascotas, propietarios y veterinarios. La aplicación incluye formularios para registrar y buscar mascotas, listado de servicios y resultados de búsqueda. Tambien incluye en esta ultima actualizacion, formularios para poder registrarse, que permitiran al usuario modificar, ingresar y eliminar infomacion de la app. A parte de poder agregar un avatar, desde el admin de Django.

Estructura del Proyecto:

El proyecto esta organizado en dos app:

- PetService: maneja la parte de infomacion de registro de propietarios, mascotas y veterinarios, a travez de formularios Django, en los cuales se puede ver, editar o eliminar informacion.
  Esta incluye:

  - Carpeta con migraciones.
  - Carpeta con archivos 'static'.
  - Carpeta con los templates html.
  - Archivos .py: **init**, admin, apps, forms, models, tests, urls y views.

- usuarios: se encarga del registro, edicion, login y logout de los usuarios, los cuales pueden editar toda la informacion de PetService, solo si estan logueados.
  Esta incluye:
  - Idem PetService.

Tambien cuenta con:

- ProyectoPetService: almacena settings, urls generales, etc.
- Carpeta con archivos subidos por usuarios: media.
- db.sqlite3: base de datos sql que almacena la informacion cargada a traves de la app web.
- archivo manage.py
- Seccion de contact, con links a redes, telefono e email de contacto.
- About.
- Copyright.

Se puede acceder a la app en un servidor local:

- Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`

Funcionalidades

- Registro de Mascotas: Permite registrar nuevas mascotas con información detallada.
- Gestión de Propietarios: Registro y gestión de información de propietarios de las mascotas.
- Gestión de Veterinarios: Registro y gestión de información de veterinarios.

Requirements:

- Python 3.12.2
- Django 3.2

Autor: Pablo Bouvier, https://github.com/ErikBouvier

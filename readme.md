# Curso básico de Django

## Introducción

### ¿Qué es Django?

Uno de los frameworks más populares para crear web apps. Es gratis y Open Source.

Instagram, Pinterest, National Geographic y Platzi usan Django.

[Django](https://www.djangoproject.com/) es rápido, seguro y escalable.

### Instalación de Django

Primero, [creamos nuestro entorno virtual](https://github.com/Mike-droid/CursoPythonIntermedio#el-primer-paso-profesional-creaci%C3%B3n-de-un-entorno-virtual).

Y ya dentro hacemos `pip install django`.

Finalmente, iniciamos el proyecto con `django-admin startproject 'nombre_del_proyecto'`.

### Explorando los archivos que creó Django

- __init__.py indica que es un paquete
- asgi.py y wsgi.py son archivos que sirven para el despliegue a producción del proyecto
- settings.py son configuraciones como BD, zona horaria, lenguaje, etc.
- urls.py es el archivo que tiene las rutas del proyecto.

### El servidor de desarrollo

Entramos a la carpeta del proyecto y hacemos `py manage.py runserver` para iniciar el servidor de Django.

### Nuestro primer proyecto: Premios Platzi App

Un __proyecto__ en Django, es un __conjunto de aplicaciones__.

Ejemplo: Instagram es un proyecto de Django, que tiene varias aplicaciones, como:

- Feed (donde se cargan las fotos)
- Stories
- Messages
- Etc

### Nuestro primer proyecto: Premios Platzi App 2

Para crear aplicaciones en Django hacemos `py manage.py startapp 'nombre_de_la_app'`.

En el archivo principal de urls.py podemos indicar qué rutas tendrá nuestro proyecto.

Además, podemos crear apps que tendrán más archivos urls.py para manejar las rutas de cada respectiva app y que trabajen dentro del mismo proyecto.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]

```

Ese es el urls.py principal y en el de una app particular, podemos tener, por ejemplo:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index")
]

```

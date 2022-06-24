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

### Ajustando el archivo settings.py

Por defecto, Django solo admite bases de datos relacionales.

[Documentación de Settings](https://docs.djangoproject.com/en/4.0/ref/settings/)

[List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## Models

### ¿Qué es ORM? ¿Qué es un modelo?

ORM -> Object Relational Mapping

Se trata de relacionar una RBD (Base de datos relacional) con la POO.

Cada archivo de Python será un 'modelo' (que representa una tabla de las BBDD) y se crea con clases.

Cada atributo de la clase, es la representación de las columnas.

Y los tipos de datos de las columnas, serán las clases dentro de los atributos.

### Creando un diagrama entidad-relación para nuestro proyecto

| questions                |
| ------------------------ |
| id -> int                |
| question_text -> varchar |
| pub_date -> datetime     |

relación uno a muchos con

| choices                |
| ---------------------- |
| id -> int              |
| question -> int        |
| choice_text -> varchar |
| votes -> int           |

### Creando los modelos Question y Choice

Comandos de la clase:

- `py manage.py makemigrations 'nombre_de_la_app'` -> Django describe toda la creación de las tablas de las BBDD.
- `py manage.py migrate` -> Django toma el archivo creado con el comando anterior y lo ejecuta en la BBDD.

## Interactive Shell

### La consola interactiva de Django

Ingresamos a la shell de Django con `py mange.py shell`

Y desde aquí trabajamos como lo haríamos normalmente en Python teniendo acceso a los módulos y paquetes de nuestro proyecto.

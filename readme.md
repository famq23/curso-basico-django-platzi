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

```python
(InteractiveConsole)
>>> from polls.models import Choice, Question
>>> Question.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text='¿Cuál es el mejor curso de Platzi?', pub_date=timezone.now())
>>> q.save()
```

### El método \_\_str\_\_

Agregamos el método de `def __str__` a ambas clases y podemos obtener mejor información en la shell.

```python
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>]>
>>>
```

### Filtrando los objetos creados desde la consola interactiva

_protip_: Para limpiar la terminal en Python desde Windows, escribe:

```python
>>> import os
>>> os.system('cls')
```

__protip__: Usando `__` en los atributos, Django nos permite hacer búsquedas más complejas sobre los datos.

```python
>>> Question.objects.get(pub_date__year=timezone.now().year)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\migue\Desktop\Desktop_files\CURSOS\platzi\curso_basico_django\venv\lib\site-packages\django\db\models\manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\migue\Desktop\Desktop_files\CURSOS\platzi\curso_basico_django\venv\lib\site-packages\django\db\models\query.py", line 499, in get
    raise self.model.MultipleObjectsReturned(
polls.models.Question.MultipleObjectsReturned: get() returned more than one Question -- it returned 3!
```

### El método filter

```python
>>> Question.objects.filter(pk=1)
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>]>
>>> Question.objects.filter(pk=2)
<QuerySet [<Question: ¿Quién es el mejor profesor de Platzi?>]>
>>> Question.objects.filter(pk=4)
<QuerySet []>
>>> Question.objects.filter(question_text__startswith='¿Cuál')
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>, <Question: ¿Cuál es la mejor escuela de Platzi?>]>
>>> Question.objects.filter(pub_date__year=timezone.now().year)
<QuerySet [<Question: ¿Cuál es el mejor curso de Platzi?>, <Question: ¿Quién es el mejor profesor de Platzi?>, <Question: ¿Cuál es la mejor
escuela de Platzi?>]>
>>>
```

### Accediendo al conjunto de respuestas

```python
>>> q = Question.objects.get(pk=1)
>>> q
<Question: ¿Cuál es el mejor curso de Platzi?>
>>> q.choice_set.all()
<QuerySet []>
>>> q.choice_set.create(choice_text="Curso Básico de Python", votes=0)
<Choice: Curso Básico de Python>
>>> q.choice_set.create(choice_text="Curso de Fundamentos de Ingeniería de Software", votes=0)
<Choice: Curso de Fundamentos de Ingeniería de Software>
>>> q.choice_set.create(choice_text="Curso de Elixir", votes=0)
<Choice: Curso de Elixir>
>>> q.choice_set.all()
<QuerySet [<Choice: Curso Básico de Python>, <Choice: Curso de Fundamentos de Ingeniería de Software>, <Choice: Curso de Elixir>]>
>>> q.choice_set.count()
3
>>> Choice.objects.filter(question__pub_date__year=timezone.now().year)
<QuerySet [<Choice: Curso Básico de Python>, <Choice: Curso de Fundamentos de Ingeniería de Software>, <Choice: Curso de Elixir>]>
>>>
```

## Django Admin

### El administrador de Django

__Comando súper peligroso__: `py manage.py createsuperuser`

¿Por qué es peligroso? Porque crearemos un usuario que tenga todo el control de la base de datos y este usuario solamente debe ser usado por el administrador de la BBDD.

Cuando asignamos un nombre de usuario, correo y contraseña, haremos lo siguiente:

Debemos entrar al archivo admin.py de nuestras apps y hacer que los modelos sean disponibles para la ruta localhost:8000/admin.

## Views

### ¿Qué son las views o vistas?

Django usa el modelo MTV -> Model Template View.

Django es un fullstack framework. En el backend tenemos las views y en el frontend las templates.

Una vista tiene:

- Función -> Function Based Views
- Clase -> Generic Views

### Creando vistas para la aplicación

Creamos las vistas en views.py:

```python
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are in the index page from Premios Platzi App")


def detail(request, question_id):
    return HttpResponse(f'You are watching the question # {question_id}')


def results(request, question_id):
    return HttpResponse(f'You are watching the results from the question # {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting to the question # {question_id}')

```

Y las importamos en el archivo urls.py:

```python
from django.urls import path

from . import views

urlpatterns = [
    # * ex: /polls/
    path('', views.index, name="index"),
    # * ex: /polls/3
    path('<int:question_id>/', views.detail, name="detail"),
    # * ex: /polls/3/results
    path('<int:question_id>/results/', views.results, name="results"),
    # * ex: /polls/3/vote
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

```

### Templates en Django

Hacemos una configuración en settings.json para que VS Code use emmet en los templates de Django:

```json
"emmet.includeLanguages":{
    "django-html": "html"
}
```

### Creando el template del home

Conectamos a los templates con las views:

index.html:

```python
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li><a href="/polls/{{ question.id }}">{{ question.question_text }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}
```

views.py:

```python
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        # * La variable ahora está disponible en index.html
        "latest_question_list": latest_question_list
    })
```

### Elevando el error 404

Django tiene un shortcut que es `get_object_or_404` justamente para este tipo de casos.

### Utilizando la etiqueta url para evitar el hard coding

Conectamos urls.py con los templates:

```python
from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # * ex: /polls/
    path('', views.index, name="index"),
    # * ex: /polls/3
    path('<int:question_id>/', views.detail, name="detail"),
    # * ex: /polls/3/results
    path('<int:question_id>/results/', views.results, name="results"),
    # * ex: /polls/3/vote
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

```

```python
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <li>
    <a href="{% url 'polls:detail' question.id %}"
      >{{ question.question_text }}</a
    >
    {% comment %} polls sale del app_name y detail sale del name de la vista en
    urls.py {% endcomment %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}

```

## Forms

### Formularios: lo básico

__pro tip__: SIEMPRE usa `{% csrf_token %}` en los formularios POST para evitar ataques de hacking.

### Creando la vista vote

Es buena práctica hacer redirect después de que el usuario usó un formulario

### Creando la vista results

Para que pluralize funcione, no debe de haber espacios:

```python
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>
    {{ choice.choice_tex }} -- {{ choice.votes }} vote{{choice.votes|pluralize}}
  </li>
  {% endfor %}
</ul>
<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

## Generic Views

### Clase Generic Views

Las Generic views son funciones basadas en clases (POO).

[Classy Class-Based Views](http://ccbv.co.uk/)

### Implementado generic views en la aplicación

¿Cuándo usar Generic y Function views?

Si sigues el modelo de la BBDD, usa Generic Views. Si haces algo más complejo, usa Function-based views.

> Si se puede, Generic, si no se puede, Function.

## Examen

- ¿Cuál de los siguientes métodos devuelve un registro que cumpla una condición de una tabla?: `model.objects.if` 💢
- ¿Qué es una view o vista?: Una página web pública de nuestro proyecto
- Cuando se tiene una vista con una funcionalidad común en el desarrollo web, debería usar: Generic Views
- ¿Cuál de los siguientes comandos, para iniciar la consola interactiva de Django, está escrito correctamente?: `python manage.py shell`
- ¿Qué es Django?: Un framework de desarrollo web con Python, gratis y open source
- ¿Cuál de los siguientes métodos devuelve todos los registros de una tabla?: `model.objects.all`
- ¿Cuál de los siguientes comandos para crear un proyecto en Django está escrito correctamente?: `django-admin startproject premiosplatziapp`
- ¿Qué es un proyecto en Django?: Un conjunto de aplicaciones independientes
- ¿Qué contiene el archivo manage.py?: El código que hace que el comando django-admin funcione, y permite también ejecutar comandos específicos sobre el proyecto
- ¿Qué contiene el archivo asgi.py?: El código necesariopara conectar nuestro proyecto con un servidor, una vez que hagamos deploy del mismo
- ¿Cuál de los siguientes comandos, para crear una aplicación en Django, está escrito correctamente?: `python manage.py startapp polls`
- ¿Cuál de los siguientes comandos, para inicializar un super usuario en el administrador de Django, está escrito correctamente?: `python manage.py createsuperuser`
- ¿Qué es ORM (Object Relational Mapping)?: Es una técnica que utilizan ciertas librerías y frameworks, como Django, para replicar con POO, la estructura de una BBDD.
- ¿A qué equivale una columna de una tabla de una base de datos relacional (en programación orientada a objetos) con el ORM de Django?: atributo
- ¿Qué es el administrador de Django?: Una interfaz web, ya construida, que permite ver, crear, modificar y eliminar los diferentes registros de cada uno de los modelos que hayamos definido en nuestro proyecto.
- Al administrador de datos...: Podemos usarlo desde el principio, ya que viene preinstalado en Django
- ¿Cuál de los siguientes métodos devuelve un conjunto de registros que cumplan una condición de una tabla?: `models.objects.filter`
- ¿Cuál de los siguientes es un motor de base de datos soportado nativamente por Django?: Todas
- ¿Cuál de las siguientes es una característica de Django?: Todas
- ¿Para qué sirve la consola interactiva de Django?: Nos permite ejecutar comandos especiales que la consola de Python no 💢
- ¿Qué contiene el archivo urls.py?: Las direcciones web a las que se puede acceder en nuestro proyecto
- Una aplicación es un conjunto de proyectos independientes: falso
- Una vista es responsable de una de dos cosas: ambas
- ¿A qué equivale una tabla de una base de datos relacional (en programación orientada a objetos) con el ORM de Django?: A un modelo (clase)
- ¿Cuál de las siguientes empresas utiliza Django en su backend?: Instagram
- Las migrations son archivos históricos de todas las actualizaciones que hicimos sobre nuestros modelos, que Django utiliza para replicar en la base de datos, las clases que nosotros creamos: verdadero
- ¿Cuál de los siguientes archivos no es creado automáticamente por Django?: urls.py 💢
- Django está en el top 3 de frameworks de desarrollo web con Python: Verdadero
- ¿Cuál de las siguientes es una variable inexistente en el archivo settings.py?: APP_CONTAINER
- ¿Cuál de los siguientes comandos, para iniciar el servidor de desarrollo en Django, está escrito correctamente?: `py manage.py runserver`

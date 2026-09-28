# Ruta de aprendizaje

Recorre los apuntes en orden. Después de cada uno, cambia algo pequeño en el proyecto y escribe qué observaste.

## 01 — Instalar y leer el proyecto

Observa `manage.py`, `config/settings.py` y `config/urls.py`. Ejecuta el servidor y localiza cómo Django encuentra la configuración.

## 02 — Modelos y ORM

Lee `learning/models.py`. Compara cada campo con una columna de PostgreSQL y ejecuta `python manage.py makemigrations --check`.

## 03 — URLs y views

Sigue una petición desde `web/urls.py` hasta `HomeView` o `NoteDetailView`. Cambia temporalmente un texto para ver el recorrido completo.

## 04 — Templates

Empieza en `templates/base.html` y sigue la herencia hasta `web/home.html`. Identifica contexto, bucles, condicionales y `{% url %}`.

## 05 — Formularios y autenticación

Lee `web/forms.py` y las vistas protegidas con `LoginRequiredMixin`. Intenta visitar `/notes/new/` sin iniciar sesión y observa el redireccionamiento.

## 06 — API REST

Abre `/api/docs/`. Compara `NoteSerializer` con `NoteForm`: ambos validan o representan datos, pero sirven a clientes distintos.

## Método de estudio

1. Lee el apunte y el archivo que menciona.
2. Ejecuta una petición o cambia una línea pequeña.
3. Escribe una nota nueva explicando el resultado con tus propias palabras.
4. Añade una prueba cuando el comportamiento sea importante.


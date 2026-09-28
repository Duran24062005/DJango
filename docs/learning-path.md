# Ruta de aprendizaje

Recorre los apuntes en orden. No intentes memorizar todo en una lectura: lee, ejecuta un cambio pequeño, rompe algo de forma controlada y escribe qué observaste. Cada etapa debe terminar con una evidencia en el código o en una prueba.

## 01 — Instalar y leer el proyecto

Observa `manage.py`, `config/settings.py` y `config/urls.py`. Ejecuta el servidor, cambia el puerto y localiza cómo Django encuentra la configuración. Después explica por qué `.env` no debe subirse a Git y qué diferencia hay entre una aplicación y un proyecto.

## 02 — Modelos y ORM

Lee `learning/models.py`. Compara cada campo con una columna de PostgreSQL, revisa las relaciones y ejecuta `python manage.py makemigrations --check`. Añade un campo pequeño, genera la migración, aplícala y consulta un objeto desde el shell.

## 03 — URLs y views

Sigue una petición desde `web/urls.py` hasta `HomeView` o `NoteDetailView`. Dibuja el recorrido navegador → URLconf → view → contexto → template. Cambia temporalmente un filtro y compara un `404` con un `NoReverseMatch`.

## 04 — Templates

Empieza en `templates/base.html` y sigue la herencia hasta `web/home.html`. Identifica contexto, bucles, condicionales, `{% url %}`, `{% empty %}` y autoescape. Añade un estado vacío para una búsqueda sin resultados.

## 05 — Formularios y autenticación

Lee `web/forms.py` y las vistas protegidas con `LoginRequiredMixin`. Intenta visitar `/notes/new/` sin iniciar sesión, envía un formulario inválido y observa el token CSRF. Luego explica la diferencia entre autenticación, autorización y validación.

## 06 — API REST

Abre `/api/docs/`. Compara `NoteSerializer` con `NoteForm`: ambos validan o representan datos, pero sirven a clientes distintos. Prueba búsqueda, filtros, un slug inexistente y una operación de escritura sin autenticación.

## Método de estudio

1. Lee el apunte y el archivo que menciona.
2. Ejecuta una petición o cambia una línea pequeña.
3. Escribe una nota nueva explicando el resultado con tus propias palabras.
4. Añade una prueba cuando el comportamiento sea importante.

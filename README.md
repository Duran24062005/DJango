# Django Notes

Una wiki personal para aprender Django construyendo. El proyecto guarda apuntes en Markdown, los organiza como una ruta de estudio y expone el mismo conocimiento mediante una web tradicional y una API REST independiente.

## Qué vas a aprender

La aplicación está escrita para que puedas leer el código en capas: `learning/` contiene el dominio y los modelos; `web/` contiene templates, formularios y vistas HTML; `webapi/` contiene serializers, viewsets y routers JSON; `config/` conecta las piezas.

## Requisitos

- Python 3.12+
- Docker y Docker Compose
- PostgreSQL 16 (Docker lo provee)

## Instalación local

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
# Si usas una base administrada, completa DATABASE_URL en .env y omite Docker.
docker compose up -d db       # solo para PostgreSQL local
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_learning
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`. El usuario propietario puede entrar en `/login/`, crear apuntes desde `Nuevo apunte` y administrarlos también desde `/admin/`.

### Configuración de la base de datos

La aplicación carga `.env` automáticamente. La prioridad de configuración es:

1. `DATABASE_URL`, recomendada para una base administrada.
2. `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST` y `POSTGRES_PORT`.
3. Valores locales predeterminados (`django_wiki` en `localhost:5432`).

Cuando existe `DATABASE_URL`, Django la utiliza con SSL obligatorio y mantiene las conexiones durante 10 minutos. `DATABASE_URL_UNPOOLED` se documenta para proveedores que separan conexiones de aplicación y migraciones, pero no reemplaza automáticamente a `DATABASE_URL`.

No subas `.env` al repositorio. `.env.example` contiene nombres y valores ficticios para que cada entorno pueda reconstruir la configuración sin exponer credenciales.

### Despliegue en Vercel

En los entornos de Vercel configura `DJANGO_ALLOWED_HOSTS` con el dominio público de producción, por ejemplo `django-wiki-eight.vercel.app`. Vercel también expone `VERCEL_URL` y `VERCEL_PROJECT_PRODUCTION_URL`; Django los añade automáticamente a `ALLOWED_HOSTS` cuando están disponibles. Las peticiones HTTPS de esos dominios también quedan autorizadas para CSRF mediante `CSRF_TRUSTED_ORIGINS`.

## API

La API está separada de la web y usa JSON:

| Recurso | URL | Acceso |
|---|---|---|
| Apuntes | `/api/notes/` | lectura pública; escritura autenticada |
| Categorías | `/api/categories/` | lectura pública |
| Etiquetas | `/api/tags/` | lectura pública |
| Esquema OpenAPI | `/api/schema/` | lectura pública |
| Swagger UI | `/api/docs/` | lectura pública |

Ejemplo: `curl http://127.0.0.1:8000/api/notes/?search=modelos`.

## Ruta de aprendizaje

Lee [`docs/learning-path.md`](docs/learning-path.md) en orden. Cada apunte cargado por `seed_learning` conecta una idea con el código que la implementa. El [`PRD`](docs/PRD.md) explica las decisiones del proyecto y sus límites.

## Comandos útiles

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check
docker compose logs db
docker compose down       # detiene PostgreSQL, conserva el volumen
```

Si ya tienes otro PostgreSQL ocupando el puerto 5432, puedes ejecutar la suite aislada con `DJANGO_TESTING=true python manage.py test`; la aplicación normal continúa usando PostgreSQL.

## Ejercicios sugeridos

1. Añade un campo `estimated_minutes` al modelo de apunte.
2. Crea un filtro por etiquetas en la web.
3. Escribe una prueba para que los apuntes borrador no aparezcan públicamente.
4. Añade paginación a la API y prueba `?ordering=learning_order`.
5. Crea una categoría nueva desde el admin y documenta el aprendizaje.

## Decisiones didácticas

La primera versión prefiere explícitamente código fácil de seguir sobre abstracciones prematuras. Templates y API tienen sus propios módulos para poder estudiar cada estilo sin saltar entre capas. PostgreSQL se utiliza desde el comienzo para que los modelos y migraciones se aprendan en un contexto real.

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
docker compose up -d db
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_learning
python manage.py runserver
```

Abre `http://127.0.0.1:8000/`. El usuario propietario puede entrar en `/login/`, crear apuntes desde `Nuevo apunte` y administrarlos también desde `/admin/`.

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

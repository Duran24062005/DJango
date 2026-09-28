import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-wiki-dev-only")
DEBUG = os.getenv("DJANGO_DEBUG", "true").lower() == "true"
def _csv_env(name, default=""):
    return [value.strip() for value in os.getenv(name, default).split(",") if value.strip()]


ALLOWED_HOSTS = _csv_env("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1")
# Vercel exposes the current deployment hostname automatically. Add it when
# available so preview deployments do not fail before the app can respond.
for vercel_host in _csv_env("VERCEL_URL") + _csv_env("VERCEL_PROJECT_PRODUCTION_URL"):
    ALLOWED_HOSTS.append(vercel_host.removeprefix("https://").removeprefix("http://").rstrip("/"))
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS if host not in {"localhost", "127.0.0.1"}]

INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "django_filters", "drf_spectacular", "rest_framework", "learning", "web", "webapi",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"], "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request", "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "config.wsgi.application"
if os.getenv("DJANGO_TESTING") == "true":
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
else:
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        DATABASES = {"default": dj_database_url.parse(database_url, conn_max_age=600, ssl_require=True)}
    else:
        DATABASES = {"default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB", "django_wiki"), "USER": os.getenv("POSTGRES_USER", "django_wiki"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "django_wiki"), "HOST": os.getenv("POSTGRES_HOST", "localhost"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }}
AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend", "rest_framework.filters.SearchFilter"],
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.SessionAuthentication", "rest_framework.authentication.BasicAuthentication"],
}
SPECTACULAR_SETTINGS = {"TITLE": "Wiki Django API", "DESCRIPTION": "API de la ruta personal de aprendizaje.", "VERSION": "1.0.0"}

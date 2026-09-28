from django.core.management.base import BaseCommand
from django.utils.text import slugify
from learning.models import Category, Note, Tag

NOTES = [
    (1, "Instalar Django y entender el proyecto", "El punto de partida: entorno virtual, dependencias y el comando `startproject`.", "python -m venv .venv\npip install Django\ndjango-admin startproject config .", "fundamentals", "beginner", ["instalacion", "proyecto"]),
    (2, "Modelos: convertir conceptos en datos", "Los modelos describen la información que Django guarda en la base de datos.", "Un modelo es una clase Python que representa una tabla.\n\n```python\nclass Book(models.Model):\n    title = models.CharField(max_length=200)\n```", "fundamentals", "beginner", ["modelos", "orm"]),
    (3, "URLs y views: conectar una petición", "Aprende a dirigir una URL hacia una función o clase que sabe responder.", "La URL es el mapa; la view es la decisión. Mantener esta separación hace que el proyecto sea fácil de leer.", "web", "beginner", ["urls", "views"]),
    (4, "Templates: mostrar datos con intención", "Los templates reciben contexto y construyen HTML sin conocer los detalles de la base de datos.", "Usa herencia de templates para que navegación, tipografía y mensajes tengan un solo origen.\n\n```django\n{% extends 'base.html' %}\n{% block content %}...{% endblock %}\n```", "web", "beginner", ["templates", "html"]),
    (5, "Formularios y autenticación", "Los formularios validan entrada; la autenticación protege las acciones que cambian datos.", "Antes de guardar, valida. Antes de editar, verifica que la persona tenga permiso.", "web", "intermediate", ["formularios", "auth"]),
    (6, "Diseñar una API REST", "Una API expone recursos en JSON para clientes distintos de la web tradicional.", "En esta wiki la API vive en `webapi/`: serializers, viewsets, permisos y routers están separados de los templates.", "api", "intermediate", ["api", "rest"]),
]

class Command(BaseCommand):
    help = "Carga categorías, etiquetas y apuntes iniciales para estudiar Django."
    def handle(self, *args, **options):
        categories = {"fundamentals": ("Fundamentos", "Las piezas esenciales de Django."), "web": ("Web", "URLs, vistas, templates y formularios."), "api": ("APIs", "Diseño y consumo de APIs REST.")}
        for key, (name, description) in categories.items(): Category.objects.update_or_create(slug=key, defaults={"name": name, "description": description})
        for order, title, summary, content, category, difficulty, tag_names in NOTES:
            tags = [Tag.objects.get_or_create(slug=t, defaults={"name": t.replace("-", " ").title()})[0] for t in tag_names]
            note, _ = Note.objects.update_or_create(
                title=title,
                defaults={
                    "slug": slugify(title),
                    "summary": summary,
                    "content": content,
                    "category": Category.objects.get(slug=category),
                    "difficulty": difficulty,
                    "learning_order": order,
                    "status": Note.Status.PUBLISHED,
                },
            )
            note.tags.set(tags)
        self.stdout.write(self.style.SUCCESS(f"{len(NOTES)} apuntes iniciales cargados."))

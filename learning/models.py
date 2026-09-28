from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "categories"
    def __str__(self): return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    def __str__(self): return self.name

class Note(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Borrador"
        PUBLISHED = "published", "Publicado"
    class Difficulty(models.TextChoices):
        BEGINNER = "beginner", "Inicial"
        INTERMEDIATE = "intermediate", "Intermedio"
        ADVANCED = "advanced", "Avanzado"
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=280)
    content = models.TextField(help_text="Contenido en Markdown")
    rendered_content = models.TextField(blank=True, editable=False)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="notes")
    tags = models.ManyToManyField(Tag, blank=True, related_name="notes")
    difficulty = models.CharField(max_length=15, choices=Difficulty.choices, default=Difficulty.BEGINNER)
    learning_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["learning_order", "title"]
        indexes = [models.Index(fields=["status", "learning_order"]), models.Index(fields=["title"])]
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("note-detail", kwargs={"slug": self.slug})
    @property
    def difficulty_label(self): return self.get_difficulty_display()


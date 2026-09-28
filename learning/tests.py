from django.test import TestCase
from django.urls import reverse
from .models import Category, Note, Tag

class NoteModelTests(TestCase):
    def setUp(self): self.category = Category.objects.create(name="Web", slug="web")
    def test_note_has_unique_slug_and_category(self):
        note = Note.objects.create(title="URLs", slug="urls", summary="r", content="# URLs", category=self.category)
        self.assertEqual(str(note), "URLs"); self.assertEqual(note.category, self.category)
    def test_tags_can_be_attached(self):
        note = Note.objects.create(title="ORM", slug="orm", summary="r", content="x", category=self.category)
        note.tags.add(Tag.objects.create(name="Modelos", slug="modelos")); self.assertEqual(note.tags.count(), 1)

class WebTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Web", slug="web")
        self.note = Note.objects.create(title="Publicado", slug="publicado", summary="Resumen", content="# Hola", category=category, status=Note.Status.PUBLISHED)
    def test_home_shows_published_notes(self): self.assertContains(self.client.get(reverse("home")), "Publicado")
    def test_detail_renders_markdown(self): self.assertContains(self.client.get(self.note.get_absolute_url()), "Hola")
    def test_create_requires_login(self): self.assertEqual(self.client.get(reverse("note-create")).status_code, 302)


import bleach
import markdown
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from learning.models import Category, Note, Tag
from .forms import NoteForm

ALLOWED_TAGS = set(bleach.sanitizer.ALLOWED_TAGS) | {"p", "pre", "code", "h1", "h2", "h3", "h4", "blockquote", "ul", "ol", "li", "table", "thead", "tbody", "tr", "th", "td", "hr", "br"}

def render_markdown(source):
    html = markdown.markdown(source, extensions=["fenced_code", "tables", "toc"])
    return bleach.clean(html, tags=ALLOWED_TAGS, attributes={"a": ["href", "title"], "code": ["class"]}, protocols=["http", "https", "mailto"])

class HomeView(ListView):
    template_name = "web/home.html"
    context_object_name = "notes"
    def get_queryset(self): return Note.objects.filter(status=Note.Status.PUBLISHED).select_related("category").prefetch_related("tags")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["total_notes"] = Note.objects.filter(status=Note.Status.PUBLISHED).count()
        context["category_count"] = Category.objects.count()
        return context

class NoteListView(ListView):
    template_name = "web/note_list.html"
    context_object_name = "notes"
    paginate_by = 8
    def get_queryset(self):
        queryset = Note.objects.filter(status=Note.Status.PUBLISHED).select_related("category").prefetch_related("tags")
        query = self.request.GET.get("q", "").strip()
        if query: queryset = queryset.filter(Q(title__icontains=query) | Q(summary__icontains=query) | Q(content__icontains=query))
        if category := self.request.GET.get("category"): queryset = queryset.filter(category__slug=category)
        if difficulty := self.request.GET.get("difficulty"): queryset = queryset.filter(difficulty=difficulty)
        if tag := self.request.GET.get("tag"): queryset = queryset.filter(tags__slug=tag)
        return queryset.distinct()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all(); context["tags"] = Tag.objects.all(); context["difficulties"] = Note.Difficulty.choices
        return context

class NoteDetailView(DetailView):
    template_name = "web/note_detail.html"; context_object_name = "note"; model = Note; slug_field = "slug"
    def get_queryset(self): return Note.objects.filter(status=Note.Status.PUBLISHED).select_related("category").prefetch_related("tags")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs); note = self.object
        context["rendered_content"] = render_markdown(note.content)
        context["previous_note"] = Note.objects.filter(status="published", learning_order__lt=note.learning_order).order_by("-learning_order").first()
        context["next_note"] = Note.objects.filter(status="published", learning_order__gt=note.learning_order).order_by("learning_order").first()
        return context

class OwnerLoginView(LoginView):
    template_name = "registration/login.html"

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note; form_class = NoteForm; template_name = "web/note_form.html"; success_url = reverse_lazy("note-list")
    def form_valid(self, form):
        form.instance.rendered_content = render_markdown(form.instance.content)
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note; form_class = NoteForm; template_name = "web/note_form.html"
    def form_valid(self, form):
        form.instance.rendered_content = render_markdown(form.instance.content)
        return super().form_valid(form)


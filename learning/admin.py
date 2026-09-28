from django.contrib import admin
from .models import Category, Note, Tag

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("learning_order", "title", "category", "status", "difficulty", "updated_at")
    list_filter = ("status", "difficulty", "category", "tags")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)

admin.site.register(Category)
admin.site.register(Tag)


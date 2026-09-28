from rest_framework import serializers
from learning.models import Category, Note, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta: model = Category; fields = ["id", "name", "slug", "description", "order"]
class TagSerializer(serializers.ModelSerializer):
    class Meta: model = Tag; fields = ["id", "name", "slug"]
class NoteSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source="category", read_only=True)
    tags_detail = TagSerializer(source="tags", many=True, read_only=True)
    class Meta:
        model = Note
        fields = ["id", "title", "slug", "summary", "content", "rendered_content", "status", "category", "category_detail", "tags", "tags_detail", "difficulty", "learning_order", "created_at", "updated_at"]
        read_only_fields = ["rendered_content", "created_at", "updated_at"]


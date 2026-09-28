from rest_framework import permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from learning.models import Category, Note, Tag
from .serializers import CategorySerializer, NoteSerializer, TagSerializer

class OwnerWritePermission(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj): return request.method in permissions.SAFE_METHODS or request.user.is_authenticated and request.user.is_staff
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.filter(status=Note.Status.PUBLISHED).select_related("category").prefetch_related("tags")
    serializer_class = NoteSerializer; permission_classes = [OwnerWritePermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]; filterset_fields = ["category", "difficulty", "status", "tags"]; search_fields = ["title", "summary", "content"]; ordering_fields = ["learning_order", "updated_at", "title"]; lookup_field = "slug"
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all(); serializer_class = CategorySerializer; permission_classes = [permissions.AllowAny]
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all(); serializer_class = TagSerializer; permission_classes = [permissions.AllowAny]


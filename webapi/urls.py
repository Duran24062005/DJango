from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NoteViewSet, TagViewSet

router = DefaultRouter()
router.register("notes", NoteViewSet, basename="api-note")
router.register("categories", CategoryViewSet, basename="api-category")
router.register("tags", TagViewSet, basename="api-tag")
urlpatterns = router.urls


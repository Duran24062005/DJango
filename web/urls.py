from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import HomeView, NoteCreateView, NoteDetailView, NoteListView, NoteUpdateView, OwnerLoginView

urlpatterns = [
    path("", HomeView.as_view(), name="home"), path("notes/", NoteListView.as_view(), name="note-list"),
    path("notes/new/", NoteCreateView.as_view(), name="note-create"), path("notes/<slug:slug>/", NoteDetailView.as_view(), name="note-detail"),
    path("notes/<slug:slug>/edit/", NoteUpdateView.as_view(), name="note-edit"), path("login/", OwnerLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]


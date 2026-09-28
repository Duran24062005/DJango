from django import forms
from learning.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "slug", "summary", "content", "status", "category", "tags", "difficulty", "learning_order"]
        widgets = {"content": forms.Textarea(attrs={"rows": 18, "placeholder": "Escribe tu apunte en Markdown…"}), "tags": forms.CheckboxSelectMultiple()}


from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Category", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("name", models.CharField(max_length=80, unique=True)), ("slug", models.SlugField(max_length=90, unique=True)), ("description", models.TextField(blank=True)), ("order", models.PositiveIntegerField(default=0))]),
        migrations.CreateModel(name="Tag", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("name", models.CharField(max_length=50, unique=True)), ("slug", models.SlugField(max_length=60, unique=True))]),
        migrations.CreateModel(name="Note", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("title", models.CharField(max_length=180)), ("slug", models.SlugField(max_length=200, unique=True)), ("summary", models.CharField(max_length=280)), ("content", models.TextField(help_text="Contenido en Markdown")), ("rendered_content", models.TextField(blank=True, editable=False)), ("status", models.CharField(choices=[("draft", "Borrador"), ("published", "Publicado")], default="draft", max_length=12)), ("difficulty", models.CharField(choices=[("beginner", "Inicial"), ("intermediate", "Intermedio"), ("advanced", "Avanzado")], default="beginner", max_length=15)), ("learning_order", models.PositiveIntegerField(default=0)), ("created_at", models.DateTimeField(auto_now_add=True)), ("updated_at", models.DateTimeField(auto_now=True)), ("category", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="notes", to="learning.category")), ("tags", models.ManyToManyField(blank=True, related_name="notes", to="learning.tag"))]),
        migrations.AddIndex(model_name="note", index=models.Index(fields=["status", "learning_order"], name="learning_no_status_2c919c_idx")),
        migrations.AddIndex(model_name="note", index=models.Index(fields=["title"], name="learning_no_title_7e30a2_idx")),
    ]


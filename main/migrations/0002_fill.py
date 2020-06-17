from django.db import migrations


def initial_post(apps, schema_editor):
    Post = apps.get_model("main", "Post")

    Post.objects.create(content="Hello, world.")


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(initial_post),
    ]
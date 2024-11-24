# Generated by Django 4.2.16 on 2024-11-24 13:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        verbose_name="Contenido"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=200, unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de Edición"
                    ),
                ),
                ("order", models.SmallIntegerField(default=0, verbose_name="Orden")),
            ],
            options={
                "verbose_name": "página",
                "verbose_name_plural": "páginas",
                "ordering": ["order", "title"],
            },
        ),
    ]

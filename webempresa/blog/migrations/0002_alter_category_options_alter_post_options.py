# Generated by Django 4.2.16 on 2024-11-21 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "categoría", "verbose_name_plural": "categorías"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "entrada", "verbose_name_plural": "entradas"},
        ),
    ]

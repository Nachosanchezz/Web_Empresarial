# Generated by Django 4.2.16 on 2024-11-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_category_options_alter_post_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="categories",
            field=models.ManyToManyField(
                related_name="get_posts", to="blog.category", verbose_name="Categorías"
            ),
        ),
    ]
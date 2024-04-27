# Generated by Django 4.2.2 on 2023-07-16 22:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("title_en", models.CharField(max_length=255, null=True, verbose_name="title")),
                ("title_fr", models.CharField(max_length=255, null=True, verbose_name="title")),
                ("subtitle", models.CharField(blank=True, max_length=255, verbose_name="subtitle")),
                ("subtitle_en", models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle")),
                ("subtitle_fr", models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle")),
                ("meta_title", models.CharField(blank=True, max_length=255, verbose_name="meta title")),
                ("meta_title_en", models.CharField(blank=True, max_length=255, null=True, verbose_name="meta title")),
                ("meta_title_fr", models.CharField(blank=True, max_length=255, null=True, verbose_name="meta title")),
                ("meta_description", models.CharField(blank=True, max_length=255, verbose_name="meta description")),
                (
                    "meta_description_en",
                    models.CharField(blank=True, max_length=255, null=True, verbose_name="meta description"),
                ),
                (
                    "meta_description_fr",
                    models.CharField(blank=True, max_length=255, null=True, verbose_name="meta description"),
                ),
                ("description", models.TextField(blank=True, verbose_name="description")),
                ("description_en", models.TextField(blank=True, null=True, verbose_name="description")),
                ("description_fr", models.TextField(blank=True, null=True, verbose_name="description")),
                ("long_description", models.TextField(blank=True, verbose_name="long description")),
                ("long_description_en", models.TextField(blank=True, null=True, verbose_name="long description")),
                ("long_description_fr", models.TextField(blank=True, null=True, verbose_name="long description")),
            ],
            options={
                "verbose_name": "about",
                "verbose_name_plural": "about",
            },
        ),
    ]

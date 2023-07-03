# Generated by Django 4.2.2 on 2023-07-01 18:32

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Services",
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=255, null=True)),
                (
                    "meta_title",
                    models.CharField(
                        blank=True,
                        help_text="This shows at the top of the browser, usually in the tab.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "meta_description",
                    models.CharField(
                        blank=True,
                        help_text="Optimal length is roughly 155 characters",
                        max_length=180,
                        null=True,
                    ),
                ),
                ("category", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/services"
                    ),
                ),
                (
                    "short_content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                (
                    "long_content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                ("page_index_published", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(blank=True, max_length=30, null=True)),
                ("subtitle", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                ("Services", models.ManyToManyField(to="service.services")),
            ],
            options={
                "db_table": "service",
                "managed": True,
            },
        ),
    ]

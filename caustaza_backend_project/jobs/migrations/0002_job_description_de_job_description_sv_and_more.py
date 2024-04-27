# Generated by Django 4.2.2 on 2023-07-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="description_de",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
        migrations.AddField(
            model_name="job",
            name="description_sv",
            field=models.TextField(blank=True, null=True, verbose_name="description"),
        ),
        migrations.AddField(
            model_name="job",
            name="meta_description_de",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="meta description"),
        ),
        migrations.AddField(
            model_name="job",
            name="meta_description_sv",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="meta description"),
        ),
        migrations.AddField(
            model_name="job",
            name="meta_title_de",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="meta title"),
        ),
        migrations.AddField(
            model_name="job",
            name="meta_title_sv",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="meta title"),
        ),
        migrations.AddField(
            model_name="job",
            name="subtitle_de",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle"),
        ),
        migrations.AddField(
            model_name="job",
            name="subtitle_sv",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="subtitle"),
        ),
        migrations.AddField(
            model_name="job",
            name="title_de",
            field=models.CharField(max_length=255, null=True, verbose_name="title"),
        ),
        migrations.AddField(
            model_name="job",
            name="title_sv",
            field=models.CharField(max_length=255, null=True, verbose_name="title"),
        ),
    ]

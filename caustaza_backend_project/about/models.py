from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


# Create your models here.
class About(models.Model):
    """about model."""

    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    meta_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    long_description = RichTextUploadingField(max_length=250, blank=True, null=True)

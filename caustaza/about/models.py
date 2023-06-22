from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class About(models.Model):
    """About model."""

    title = models.CharField(max_length=250, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    meta_title = models.CharField(max_length=250, blank=True, null=True)
    meta_description = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    long_description = RichTextUploadingField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title

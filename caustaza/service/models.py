from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from caustaza.utils import unique_slug_generator

class Services(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=100, blank=True, null=True, help_text='This shows at the top of the browser, usually in the tab.')
    meta_description = models.CharField(max_length=180, blank=True, null=True, help_text='Optimal length is roughly 155 characters')
    category = models.CharField(max_length =250, blank=True, null=True) 
    image = models.ImageField(upload_to='images/services',blank=True, null=True)
    short_content = RichTextUploadingField(blank=True,null=True)
    long_content = RichTextUploadingField(blank=True,null=True)
    page_index_published = models.BooleanField(default=False)
  
  


    def __str__(self):
        return self.slug
    
def slug_generator(sender, instance, *args, **kwargs):
        if not instance.slug:
          instance.slug = unique_slug_generator(instance)
        
pre_save.connect(slug_generator, sender=Services)


class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    Services = models.ManyToManyField( Services)
    title = models.CharField(max_length=30, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service'

    def __str__(self):
        return self.title
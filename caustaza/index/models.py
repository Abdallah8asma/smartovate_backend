from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Pageindex(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField(max_length=1000, blank=True, null=True)
    about_title = models.CharField(max_length=255, blank=True, null=True)
    about_description = RichTextUploadingField(max_length=1000, blank=True, null=True)
    service_title = models.CharField(max_length=255 , blank=True, null=True)
    service_subtitle = models.CharField(max_length=255 , blank=True, null=True)
    service_description = models.CharField(max_length=255 , blank=True, null=True)
    feedback_title = models.CharField(max_length=255 , blank=True, null=True)
    feedback_subtitle = models.CharField(max_length=255 ,blank=True, null=True)

    call_to_action_title = models.CharField(max_length=255, blank=True, null=True)
    call_to_action_subtitle =models.CharField(max_length=255, blank=True, null=True) 

    meta_title = models.CharField(max_length=100, blank=True, null=True, help_text='This shows at the top of the browser, usually in the tab.')
    meta_description = models.CharField(max_length=180, blank=True, null=True, help_text='Optimal length is roughly 155 characters')

    def __str__(self):
        return "%s" % (self.title)


class newsletter(models.Model):
   email = models.EmailField(max_length=254, blank=True, null=True) 

   def __str__(self):
        return self.email


#model for our clients
class FeedbackClient(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='images/clients')
    description = RichTextUploadingField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User

class MyUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username

from django.db import models

class Invoice(models.Model):
    token = models.TextField()  # Field to store the encoded clientSecret

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Invoice #{self.pk}"

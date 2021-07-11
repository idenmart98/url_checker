from django.db import models
import requests

# Create your models here.
class Url(models.Model):
    address = models.URLField(unique=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    checked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
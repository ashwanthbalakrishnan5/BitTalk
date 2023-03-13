from django.db import models

# Create your models here.


class ApiKeys(models.Model):
    name = models.CharField(max_length=255)
    apiKey = models.CharField(max_length=255)
    secretKey = models.CharField(max_length=255)

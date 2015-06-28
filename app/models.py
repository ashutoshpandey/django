from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    created_at = models.DateTimeField('created_at')
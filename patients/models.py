from django.db import models

# Create your models here.
from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

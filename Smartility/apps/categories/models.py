from django.db import models

NAME_MAX_LENGTH = 32

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
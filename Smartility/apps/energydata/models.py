from django.db import models
from django.contrib.auth.models import User

from Smartility.apps.categories.models import Category

# Create your models here.
class EnergyDataPoint(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    value = models.DecimalField(max_digits=8, decimal_places=5)
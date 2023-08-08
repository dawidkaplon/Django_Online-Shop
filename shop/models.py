from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.TextField(default='')

    def __str__(self):
        return self.name


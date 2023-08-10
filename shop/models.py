from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    price = models.FloatField()
    category = models.TextField(default='')
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return self.name

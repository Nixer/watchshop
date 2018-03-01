from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WatchShop(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watchshop')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='watchshop_logo/', blank=False)

    def __str__(self):
        return self.name

class Watch(models.Model):
    watchshop = models.ForeignKey(WatchShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='watch_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

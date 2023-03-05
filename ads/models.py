from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=500)


class AdsModel(models.Model):
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField()

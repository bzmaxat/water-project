from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='catalog/images/')
    price = models.IntegerField()
    availability = models.BooleanField(default='False')


class Customer(models.Model):
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    url = models.URLField(blank=True)

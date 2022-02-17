from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Options(models.Model):
    name = models.CharField(max_length=100)
    increment = models.FloatField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Additional(models.Model):
    name = models.CharField(max_length=100, unique=True)
    maximum = models.IntegerField()
    minimum = models.IntegerField()
    options = models.ManyToManyField(Options)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='post_img')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.CharField(max_length=2000)
    additionals = models.ManyToManyField(Additional, blank=True)
    active = models.BooleanField(default=True)

    @mark_safe
    def icon(self):
        return f'<img width="30px" src="/media/{self.img}">'

    def __str__(self):
        return self.name

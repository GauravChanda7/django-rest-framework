from django.db import models

# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length=30)

    def __str__(self):
        return self.color_name


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    fav_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='people')

    def __str__(self):
        return self.name
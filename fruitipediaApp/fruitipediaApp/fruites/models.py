from django.core.validators import MinLengthValidator
from django.db import models

from validators import is_alpha_validator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name



class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[
        MinLengthValidator(2),
        is_alpha_validator
    ])
    Image_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    nutrition = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='fruits')



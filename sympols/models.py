from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
# Create your models here.

SYMBOL_DIMENTION_CHOICES = [
    ("1*1", "1*1"),
    ("2*2", "2*2"),
    ("3*2", "3*2"),
    ("4*2", "4*2"),
]


class Symbols_Collectoin(models.Model):
    name = models.CharField(max_length=100)
    dimension_of_symbols = models.CharField(max_length=5, choices=SYMBOL_DIMENTION_CHOICES)
    collection_image = models.ImageField(upload_to="Symbols_Collectoin")

    def __str__(self):
        return self.name


class symbol(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='symbols')
    collection = models.ForeignKey(Symbols_Collectoin, on_delete=models.CASCADE)
    text_to_talk = models.CharField(max_length=100)
    def __str__(self):
        return self.name


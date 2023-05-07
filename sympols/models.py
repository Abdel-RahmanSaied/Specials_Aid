from django.db import models
# Create your models here.

SYMBOL_DIMENTION_CHOICES = [
    ("1*1", "1*1"),
    ("2*2", "2*2"),
    ("3*2", "3*2"),
    ("4*2", "4*2"),
]


class Symbols_Collectoin(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    dimension_of_symbols = models.CharField(max_length=5, choices=SYMBOL_DIMENTION_CHOICES)
    collection_image = models.ImageField(upload_to='symbols')

    def __str__(self):
        return self.name


class symbol(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='symbols')
    collection = models.ForeignKey(Symbols_Collectoin, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


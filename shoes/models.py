from django.db import models

# Create your models here.
class Shoes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    descriptionShoes = models.TextField(max_length=150,default="pendiente")
    priceShoes = models.FloatField(null=True)
    imageUrl = models.TextField(default='inserte URL de la image')


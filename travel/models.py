from django.db import models


class Destination(models.Model):

    name = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

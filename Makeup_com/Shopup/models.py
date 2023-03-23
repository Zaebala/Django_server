from django.db import models

# Create your models here.


class shine(models.Model):
    name = models.CharField(max_length=100)
    brand_id = models.CharField(max_length=100)
    volume = models.IntegerField()
    price = models.IntegerField()
    info = models.TextField()
    # img = models.ImageField(upload_to="photos/")

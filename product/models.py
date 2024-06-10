from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=60)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/')

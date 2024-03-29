from django.db import models

# Create your models here.

class Destination(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    price = models.IntegerField()
    offer=models.BooleanField(default=False)
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name



from django.db import models

# Create your models here.


class fruits(models.Model):
    fruit=models.CharField(max_length=10)
    rate=models.IntegerField()
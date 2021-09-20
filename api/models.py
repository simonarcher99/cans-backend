from django.db import models

class Cans(models.Model):
    item = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField()
    

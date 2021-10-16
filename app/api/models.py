from django.db import models

class User(models.Model):
    first_name = models.CharField(blank=True, max_length=150, verbose_name="First Name")
    last_name = models.CharField(blank=True, max_length=150, verbose_name="Last Name")
    password = models.CharField(max_length=128, verbose_name="Password")
    email = models.EmailField(max_length=254, unique=True, verbose_name="Email Adress")

class Cans(models.Model):
    item = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING)
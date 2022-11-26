from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    loct = models.TextField()
    features = models.BooleanField(default=False)

class Buy_property(models.Model):

    property_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    property_description = models.CharField(max_length=100)
    property_price = models.FloatField(default=0)
   
    def __str__(self):
        return self.property_name

class Sale_property(models.Model):

    property_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    property_description = models.CharField(max_length=100)
    property_price = models.FloatField(default=0)
   
    def __str__(self):
        return self.property_name

class Rent_property(models.Model):

    property_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    property_description = models.CharField(max_length=100)
    property_price = models.FloatField(default=0)
   
    def __str__(self):
        return self.property_name

class Mortgage_property(models.Model):

    property_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    property_description = models.CharField(max_length=100)
    property_price = models.FloatField(default=0)
   
    def __str__(self):
        return self.property_name

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

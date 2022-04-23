from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    name = models.CharField(max_length=250)
    
    mobile = models.CharField(unique=True,max_length=250,blank=True)

class Customer(models.Model):
    customer = models.ForeignKey(
        User,on_delete=models.CASCADE, related_name="customer_account"
    )
    age = models.CharField(max_length=250)
    weight = models.IntegerField()
    height = models.IntegerField()
    health_condition = models.TextField()
    
    

class Trainer(models.Model):
    trainer = models.ForeignKey(
        User,on_delete=models.CASCADE,related_name="trainer_account"
    )
    certification = models.CharField(max_length=250)
    stream = models.CharField(max_length=250)
    about = models.TextField()
from django.db import models

from accounts.models import Customer, Trainer, User

# Create your models here.
class CustomerProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)
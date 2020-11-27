from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense(models.Model):
    text = models.CharField("Comments:",max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    #Email=models.EmailField(max_length=255, default="Enter your Email...")
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)
class Income(models.Model):
    text = models.CharField("Comments:",max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    #Email=models.EmailField(max_length=255, default="Enter your Email...")
    #upload = models.FileField(upload_to='uploads/')
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)

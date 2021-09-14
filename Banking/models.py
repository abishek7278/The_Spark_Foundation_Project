from django.db import models

# Create your models here.
class transferdetail(models.Model):
    name=models.CharField(max_length=50,null=True)
    sender_name=models.CharField(max_length=50,null=True)
    amount=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    
class customerdetail(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    balance=models.IntegerField()

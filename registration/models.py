from django.db import models
import uuid

class Users(models.Model):
    User_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    User_name=models.CharField(max_length=150)
    Date_of_Birth=models.DateField()
    Gender=models.CharField(max_length=5,blank=True)
    Email=models.EmailField()
    Phone_no=models.BigIntegerField()
    Password=models.CharField(max_length=128)

class Token(models.Model):
    Userid=models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    Tokens=models.CharField(max_length=500,blank=True)
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pg(models.Model):
    pid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    phone=models.CharField(max_length=15)
    type=models.CharField(max_length=10)
    image=models.ImageField(upload_to="images/",default="")
    address=models.CharField(max_length=100, default="yet to be known")
    def __str__(self):
        return self.name

class Booking(models.Model):
    by=models.ForeignKey(User,on_delete=models.CASCADE)
    booked=models.ForeignKey(Pg,on_delete=models.CASCADE)
    food=models.CharField(max_length=10)
    timeperiod=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=13 ,default="0000000000")
    type=models.CharField(max_length=13, default="Student")
    def __str__(self):
        return self.by.username


class Review(models.Model):
    by=models.ForeignKey(User,on_delete=models.CASCADE)
    to=models.IntegerField(default=1)
    ratings=models.CharField(max_length=10)
    desc=models.TextField()
    def __str__(self):
        return self.by.username
    
    
   

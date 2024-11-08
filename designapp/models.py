from django.db import models
class Register(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)

class Student(models.Model):
    rno=models.CharField(max_length=12)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=10)
    fee=models.IntegerField()
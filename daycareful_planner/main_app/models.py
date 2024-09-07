from django.db import models

# Create your models here.
class ParentInfo(models.Model):
    name = models.CharField(max_length=50)
    kidsName = models.CharField(max_length=50)
    paid = models.IntegerField()
    attendance = models.IntegerField()

class ChildInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    allergies = models.TextField(max_length=250)

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=50)
    hours = models.IntegerField()
    attendance = models.IntegerField()
    pay = models.IntegerField()
    position = models.CharField(max_length=50)
from django.db import models

class ParentInfo(models.Model):
    name = models.CharField(max_length=50)
    kidsName = models.CharField(max_length=50)
    paid = models.IntegerField()
    attendance = models.IntegerField()
    image = models.ImageField(upload_to='parent_images/', blank=True, null=True)

class ChildInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    allergies = models.TextField(max_length=250)
    image = models.ImageField(upload_to='child_images/', blank=True, null=True)

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=50)
    hours = models.IntegerField()
    attendance = models.IntegerField()
    pay = models.IntegerField()
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)
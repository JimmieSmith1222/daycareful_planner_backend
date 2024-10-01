from django.db import models
from django.contrib.auth.models import User

def get_default_user():
    return User.objects.get(username='Admin').id

class ParentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    kidsName = models.CharField(max_length=50)
    paid = models.CharField(max_length=50)
    attendance = models.IntegerField()
    image = models.ImageField(upload_to='parent_images/', blank=True, null=True)

class ChildInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    allergies = models.TextField(max_length=250)
    image = models.ImageField(upload_to='child_images/', blank=True, null=True)

class EmployeeInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    hours = models.IntegerField()
    attendance = models.IntegerField()
    pay = models.IntegerField()
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='employee_images/', blank=True, null=True)
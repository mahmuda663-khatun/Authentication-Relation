from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class AuthenticateModel(AbstractUser):
    USER_TYPE=[
        ('Admin','Admin'),
        ('User','User'),
    ]
    user_type=models.CharField(choices=USER_TYPE,null=True)

    def __str__(self):
        return self.username

class DepartmentModel(models.Model):
    dep_name=models.CharField(null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.dep_name
    
class EmployeeModel(models.Model):
    name=models.CharField(null=True)
    designation=models.TextField(null=True)
    Address=models.TextField(null=True)
    image=models.ImageField(upload_to='image/',null=True)
    department=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
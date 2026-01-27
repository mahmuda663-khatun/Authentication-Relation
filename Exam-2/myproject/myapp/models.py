from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    USER_TYPE=[
        ('Admin','Admin'),
        ('Employe','Employe'),
    ]
    user_type=models.CharField(choices=USER_TYPE,null=True)

    def __str__(self):
        return self.username
    
class DepartmentModel(models.Model):
    departname=models.CharField(null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.departname
    
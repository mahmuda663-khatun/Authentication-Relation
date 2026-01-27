from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    ROLE=[
        ('Admin','Admin'),
        ('User','User'),
    ]
    Role=models.CharField(choices=ROLE,null=True)

    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    ROLE=[
        ('student','student'),
        ('teacher','teacher'),
    ]
    Role=models.CharField(choices=ROLE,max_length=100,null=True)

    def __str__(self):
        return self.username
    
class DepartModel(models.Model):
    name=models.CharField(null=True)
    description=models.TextField(max_length=200,null=True)

    def __str__(self):
        return self.name
    
class StudentModel(models.Model):
    name=models.CharField(null=True)
    image=models.ImageField(upload_to='imag/',null=True)
    department=models.ForeignKey(DepartModel,on_delete=models.CASCADE,null=True)
    food_per=models.DecimalField(decimal_places=10,max_digits=50,null=True)
    total_fee=models.DecimalField(decimal_places=10,max_digits=50,null=True)
    food_fee=models.DecimalField(decimal_places=10,max_digits=50,null=True)

    def __str__(self):
        return self.name
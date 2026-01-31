from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserModel(AbstractUser):
    ROLE=[
        ('Admin','Admin'),
        ('Viewr','Viewr'),
    ]
    role=models.CharField(choices=ROLE,null=True)

    def __str__(self):
        return self.username
    
class CategoryModel(models.Model):
    name=models.CharField(null=True)
    description=models.TextField(max_length=100,null=True)

    def __str__(self):
        return self.name
    
class RecipeModel(models.Model):
    title=models.CharField(null=True)
    description=models.TextField(max_length=200,null=True)
    ingredients=models.CharField(null=True)
    instructions=models.TextField(null=True)
    image=models.ImageField(upload_to='image/',null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    created_by=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    update_at=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title
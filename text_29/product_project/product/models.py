from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name=models.CharField(null=True)

    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    STOCK=[
        ('Available','Available'),
        ('Out_of_stock','Out_of_stock'),
    ]
    name=models.CharField(null=True)
    unit_price=models.IntegerField(null=True)
    qty=models.IntegerField(null=True)
    total_amount=models.IntegerField(null=True)
    stock=models.CharField(choices=STOCK,max_length=200,null=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
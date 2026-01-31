from django.contrib import admin
from myapp.models import*
# Register your models here.
admin.site.register(UserModel)
admin.site.register(CategoryModel)
admin.site.register(RecipeModel)
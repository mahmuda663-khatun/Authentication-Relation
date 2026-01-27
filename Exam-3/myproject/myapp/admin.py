from django.contrib import admin
from myapp.models import*
# Register your models here.
admin.site.register(AuthenticateModel)
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)

from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('dep_list/',dep_list,name='dep_list'),
    path('dep_add/',dep_add,name='dep_add'),
    path('dep_edit/<int:id>/',dep_edit,name='dep_edit'),
    path('dep_delete/<int:id>/',dep_delete,name='dep_delete'),
    path('employeelist/',employeelist,name='employeelist'),
    path('employeeAdd/',employeeAdd,name='employeeAdd'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

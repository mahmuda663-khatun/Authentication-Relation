
from django.contrib import admin
from django.urls import path
from myapp.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('chengepass/',chengepass,name='chengepass'),
    path('dep_page/',dep_page,name='dep_page'),
    path('dep_edit/<int:id>/',dep_edit,name='dep_edit'), 
    path('dep_delete/<int:id>/',dep_delete,name='dep_delete'), 
    path('studentpage/',studentpage,name='studentpage'), 
    path('studentEdit/<int:id>/',studentEdit,name='studentEdit'), 
    path('studentDelete/<int:id>/',studentDelete,name='studentDelete'), 
]

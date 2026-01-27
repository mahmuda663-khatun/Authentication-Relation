from django.contrib import admin
from django.urls import path
from myapp.views import*
urlpatterns = [
    
    path("home/",home,name='home'),
    path("",signup,name='signup'),
    path("signin/",signin,name='signin'),
    path("signout/",signout,name='signout'),
    path("dep_list/",dep_list,name='dep_list'),
    path("dep_add/",dep_add,name='dep_add'),
    path("dep_edit/<int:id>/",dep_edit,name='dep_edit'),
    path("dep_delete/<int:id>/",dep_delete,name='dep_delete'),
    path("changepass/",changepass,name='changepass'),
]

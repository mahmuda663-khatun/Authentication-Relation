
from django.contrib import admin
from django.urls import path
from myapp.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signup,name='signup'),
    path('home/',home,name='home'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
]

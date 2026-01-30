
from django.contrib import admin
from django.urls import path
from product.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('add_cate/',add_cate,name='add_cate'),
    path('list_cate/',list_cate,name='list_cate'),
    path('edit_cate/<int:id>/',edit_cate,name='edit_cate'),
    path('delete_cate/<int:id>/',delete_cate,name='delete_cate'),
    path('productlist/',productlist,name='productlist'),
    path('productAdd/',productAdd,name='productAdd'),
    path('productEdit/<int:id>/',productEdit,name='productEdit'),
    path('productDelete/<int:id>/',productDelete,name='productDelete'),
]

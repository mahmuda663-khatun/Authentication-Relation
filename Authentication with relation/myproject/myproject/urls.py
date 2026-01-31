
from django.contrib import admin
from django.urls import path
from myapp.views import*
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout'),
    path('chengepass/',chengepass,name='chengepass'),
    path('cate_page/',cate_page,name='cate_page'),
    path('cate_edit/<int:id>/',cate_edit,name='cate_edit'),
    path('cate_delete/<int:id>/',cate_delete,name='cate_delete'),
    path('recipe_page/',recipe_page,name='recipe_page'),
    path('recipe_edit/<int:id>',recipe_edit,name='recipe_edit'),
    path('recipe_delete/<int:id>',recipe_delete,name='recipe_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
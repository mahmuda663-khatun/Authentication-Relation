from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
 
    path('departments/', views.department_list, name='department_list'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),
    
  
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    

    path('salary/', views.salary_list, name='salary_list'),
    path('salary/<int:pk>/edit/', views.salary_update, name='salary_update'),
    path('salary/<int:pk>/delete/', views.salary_delete, name='salary_delete'),
    
]

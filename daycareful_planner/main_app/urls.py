from django.urls import path
from . import views
from .views import child_list, child_detail, child_create, child_edit, child_delete, employee_list, employee_create, employee_edit, employee_delete, employee_detail

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
    path('parents/', views.parent_list, name='parent_list'),
    path('parents/<int:id>/', views.parent_detail, name='parent_detail'),
    path('parents/new/', views.parent_create, name='parent_create'),
    path('parents/<int:id>/edit/', views.parent_edit, name='parent_edit'),
    path('parents/<int:id>/delete/', views.parent_delete, name='parent_delete'),
    path('children/', child_list, name='child_list'),
    path('children/<int:id>/', child_detail, name='child_detail'),
    path('children/add/', child_create, name='child_create'),
    path('children/<int:id>/edit/', child_edit, name='child_edit'),
    path('children/<int:id>/delete/', child_delete, name='child_delete'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', employee_create, name='employee_create'),
    path('employees/<int:id>/', employee_detail, name='employee_detail'),
    path('employees/<int:id>/edit/', employee_edit, name='employee_edit'),
    path('employees/<int:id>/delete/', employee_delete, name='employee_delete'),
]

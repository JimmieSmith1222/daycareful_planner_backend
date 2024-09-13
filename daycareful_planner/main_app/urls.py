from django.urls import path
from . import views
from .views import child_list, child_detail, child_create, child_edit, child_delete

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
]

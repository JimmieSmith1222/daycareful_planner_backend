from django.urls import path
from . import views

urlpatterns = [
    path('', views.parent_list, name='parent_list'),
    path('parents/', views.parent_list, name='parent_list'),
    path('parents/<int:id>/', views.parent_detail, name='parent_detail'),
    path('parents/new/', views.parent_create, name='parent_create'),
    path('parents/<int:id>/edit/', views.parent_edit, name='parent_edit'),
    path('parents/<int:id>/delete/', views.parent_delete, name='parent_delete'),
]

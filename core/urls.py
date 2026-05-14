from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('admin-portal/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/program/add/', views.edit_program, name='add_program'),
    path('programs/edit/<int:pk>/', views.edit_program, name='edit_program'),
    path('dashboard/program/delete/<int:pk>/', views.delete_program, name='delete_program'),
    path('message/delete/<int:pk>/', views.delete_message, name='delete_message'),
    path('message/view/<int:pk>/', views.view_message, name='view_message'),
]
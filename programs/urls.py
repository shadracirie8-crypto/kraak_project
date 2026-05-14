from django.urls import path
from . import views

urlpatterns = [
    # ... tes autres routes (home, contact, services)
    path('', views.programmes_view, name='programmes'),
]
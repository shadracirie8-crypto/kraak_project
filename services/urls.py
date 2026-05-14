from django.urls import path

from contact import views
from .views import *

urlpatterns = [
    path('', services_view, name='services'),
    path('<int:pk>/', service_detail_view, name='service_detail'),
]
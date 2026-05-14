from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Connexion / Déconnexion (Vues intégrées de Django)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Inscription et Dashboard
   
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('signup/', views.sign_view, name='signup'),
    path('success/', views.redirect_after_login, name='redirect_after_login'),
]
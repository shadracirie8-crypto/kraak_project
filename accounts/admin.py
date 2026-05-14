from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # On ajoute le champ 'role' dans l'affichage de l'admin
    fieldsets = UserAdmin.fieldsets + (
        ('Options de rôle', {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role', 'is_staff']

admin.site.register(User, CustomUserAdmin)
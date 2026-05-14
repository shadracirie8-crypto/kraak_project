from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.contrib.auth.forms import UserCreationForm
from .models import User



class ClientSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'CLIENT' # On force le rôle à CLIENT par défaut
        if commit:
            user.save()
        return user
    
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)
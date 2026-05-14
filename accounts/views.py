from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm

# 1. La fonction d'aiguillage
@login_required
def redirect_after_login(request):
    """Redirige dynamiquement selon le rôle de l'utilisateur."""
    if request.user.is_staff or request.user.is_superuser:
        return redirect('admin_dashboard')
    return redirect('user_dashboard')

# 2. Vue d'inscription mise à jour
def sign_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Bienvenue chez KRAAK, {user.username} !")
            # On utilise l'aiguillage au lieu d'une redirection fixe
            return redirect('redirect_after_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# 3. Dashboard Utilisateur (Client) sécurisé
@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

# 4. Dashboard Admin sécurisé (Seulement pour le staff)
@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
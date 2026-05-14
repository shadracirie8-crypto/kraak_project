# Django core shortcuts
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Gestion des messages flash (renommé pour éviter les conflits avec ton modèle Message)
from django.contrib import messages as django_messages

# Modèles de l'application courante (core)
from .models import Statistic, Partner, Testimonial, TeamMember

# Modèles des autres applications
from services.models import Service
from programs.models import Program, ProgramFeature
from contact.models import ContactMessage as Message  # On le renomme ici pour ton code
from django.contrib import messages



def home(request):
    statistics = Statistic.objects.all()
    services = Service.objects.all()
    programs = Program.objects.filter(is_active=True)
    testimonials = Testimonial.objects.all()
    partners = Partner.objects.all()

    context = {
        'statistics': statistics,
        'services': services,
        'programs': programs,
        'testimonials': testimonials,
        'partners': partners,
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')



@login_required
def admin_dashboard(request):
    context = {
        'messages': Message.objects.all().order_by('-created_at'),
        'programs': Program.objects.all(),
        'partners': Partner.objects.all(),
        'services': Service.objects.all(),
        'team': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'stats': Statistic.objects.all(),
    }
    return render(request, 'dashboard.html', context)


# Liste des programmes (déjà gérée dans ton dashboard, mais utile ici aussi)
def manage_programs(request):
    programs = Program.objects.all()
    return render(request, 'admin/manage_programs.html', {'programs': programs})

# Création ou Modification
def edit_program(request, pk=None):
    # Si pk est présent, on modifie, sinon on crée un nouveau
    program = get_object_or_404(Program, pk=pk) if pk else None
    
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        duration = request.POST.get('duration')
        price = request.POST.get('price')
        is_active = request.POST.get('is_active') == 'on'
        image = request.FILES.get('image')

        # 1. Sauvegarde du Programme
        if program:
            program.title = title
            program.description = description
            program.duration = duration
            program.price = price if price else None
            program.is_active = is_active
            if image:
                program.image = image
            program.save()
            messages.success(request, f"Le programme '{title}' a été mis à jour.")
        else:
            program = Program.objects.create(
                title=title,
                description=description,
                duration=duration,
                price=price if price else None,
                is_active=is_active,
                image=image
            )
            messages.success(request, f"Le programme '{title}' a été créé avec succès.")

        # 2. Gestion des Features (Points clés)
        # On récupère la liste des titres envoyés par le JavaScript
        feature_titles = request.POST.getlist('features[]')
        
        # Approche simple : on supprime les anciennes et on recrée les nouvelles
        program.features.all().delete()
        for f_title in feature_titles:
            if f_title.strip(): # On ignore les champs vides
                ProgramFeature.objects.create(program=program, title=f_title)

        return redirect('admin_dashboard')

    return render(request, 'edit_program.html', {'program': program})
# Suppression (DELETE)
def delete_program(request, pk):
    program = get_object_or_404(Program, pk=pk)
    program.delete()
    messages.error(request, "Programme supprimé.")
    return redirect('admin_dashboard')


def delete_message(request, pk):
    try:
        # On essaie de récupérer le message
        message_obj = Message.objects.get(pk=pk)
        message_obj.delete()
        django_messages.success(request, "Le message a été supprimé avec succès.")
    except Message.DoesNotExist:
        # Si l'ID n'existe pas, on affiche une erreur discrète au lieu d'une page 404
        django_messages.error(request, "Ce message a déjà été supprimé ou n'existe pas.")
    
    return redirect('admin_dashboard')


def view_message(request, pk):
    # On utilise toujours 'Message' (notre alias pour ContactMessage)
    message_obj = get_object_or_404(Message, pk=pk)
    
    return render(request, 'view_message.html', {
        'msg': message_obj
    })
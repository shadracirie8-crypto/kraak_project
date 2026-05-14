from django.shortcuts import render
from .models import Program

def programmes_view(request):
    # On récupère uniquement les programmes cochés comme "is_active"
    programs = Program.objects.filter(is_active=True).prefetch_related('features')
    
    return render(request, 'programmes.html', {'programs': programs})



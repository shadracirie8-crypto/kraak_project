from django.shortcuts import get_object_or_404, render

from services.models import Service

def services_view(request):
    """
    Affiche la page de présentation des services de Kraak Consulting.
    """
    return render(request, 'services.html')

def service_detail_view(request, pk):
    # On récupère le service par sa clé primaire (ID)
    service = get_object_or_404(Service.objects.prefetch_related('details'), pk=pk)
    return render(request, 'details_service.html', {'service': service})    
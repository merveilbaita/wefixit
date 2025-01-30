from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Devis
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Devis
from django.views.generic import CreateView
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def propos(request):
    return render(request, 'propos.html')

def devis(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        devis = Devis(service=service)
        
        if service == 'solaire':
            devis.type_batiment = request.POST.get('typeBatiment')
            devis.nombre_pieces = request.POST.get('nombrePieces')
            
            # Récupération des appareils
            appareils = []
            noms = request.POST.getlist('appareil_nom[]')
            puissances = request.POST.getlist('appareil_puissance[]')
            durees = request.POST.getlist('appareil_duree[]')
            
            for i in range(len(noms)):
                appareils.append({
                    'nom': noms[i],
                    'puissance': puissances[i],
                    'duree': durees[i]
                })
            devis.appareils = appareils
                
        elif service == 'reparation':
            devis.modele_machine = request.POST.get('modeleMachine')
            devis.fabricant = request.POST.get('fabricant')
            devis.diagnostic_client = request.POST.get('diagnosticClient')
            
        elif service == 'antiIncendie':
            devis.type_etablissement = request.POST.get('typeEtablissement')
            devis.superficie = request.POST.get('superficie')
            devis.equipements_souhaites = request.POST.getlist('equipements[]')
            
        elif service == 'securiteElectronique':
            devis.type_site = request.POST.get('typeSite')
            devis.nombre_points_acces = request.POST.get('nombrePoints')
            devis.services_souhaites = request.POST.getlist('services[]')
            
        elif service == 'jeuxVideo':
            devis.type_console = request.POST.get('typeConsole')
            devis.modele_console = request.POST.get('modeleConsole')
            devis.probleme_console = request.POST.get('problemeConsole')
            devis.symptomes = request.POST.getlist('symptomes[]')
            devis.accessoires = request.POST.get('accessoires')
            
        devis.save()
        messages.success(request, 'Votre demande de devis a été envoyée avec succès!')
        return redirect('devis')
        
    return render(request, 'devis.html')

def devis_success(request):
    return render(request, 'devis.html')


def services(request):
    return render(request, 'services.html')
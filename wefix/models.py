from django.db import models

# Create your models here.


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=100)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom + ' ' + self.prenom

    class Meta:
        ordering = ['-date_envoi']



from django.db import models

class Devis(models.Model):
    SERVICE_CHOICES = [
        ('solaire', 'Énergie Solaire'),
        ('reparation', 'Réparation/Maintenance'),
        ('antiIncendie', 'Équipements Anti-Incendie'),
        ('securiteElectronique', 'Sécurité Électronique'),
        ('jeuxVideo', 'Consoles de Jeux'),
        ('electricite', 'Électricité'),
        ('evaluationEnvironnementale', 'Évaluation Environnementale'),
    ]
    
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    # Champs pour service solaire
    type_batiment = models.CharField(max_length=50, blank=True, null=True)
    nombre_pieces = models.PositiveIntegerField(blank=True, null=True)
    appareils = models.JSONField(default=list, blank=True)
    
    # Champs pour service réparation
    modele_machine = models.CharField(max_length=100, blank=True, null=True)
    fabricant = models.CharField(max_length=100, blank=True, null=True)
    diagnostic_client = models.TextField(blank=True, null=True)
    
    # Champs pour équipements anti-incendie
    type_etablissement = models.CharField(max_length=50, blank=True, null=True)
    superficie = models.PositiveIntegerField(blank=True, null=True)
    equipements_souhaites = models.JSONField(default=list, blank=True)
    
    # Champs pour sécurité électronique
    type_site = models.CharField(max_length=50, blank=True, null=True)
    nombre_points_acces = models.PositiveIntegerField(blank=True, null=True)
    services_souhaites = models.JSONField(default=list, blank=True)
    
    # Champs pour consoles de jeux
    type_console = models.CharField(max_length=50, blank=True, null=True)
    modele_console = models.CharField(max_length=100, blank=True, null=True)
    probleme_console = models.TextField(blank=True, null=True)
    symptomes = models.JSONField(default=list, blank=True)
    accessoires = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Devis {self.service} - {self.date_creation.strftime('%d/%m/%Y')}"

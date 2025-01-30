from django.db import models
from django.utils import timezone

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='articles')
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-date_publication']
        
    def __str__(self):
        return self.titre

from django.shortcuts import render
from .models import Article

def blog(request):
    # Récupérer tous les articles en les ordonnant selon le champ défini dans le modèle
    articles = Article.objects.all()
    return render(request, 'blog/blog.html', {'articles': articles})

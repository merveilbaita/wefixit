from django.urls import path
from Src import settings
from wefix.views import index, contact, propos,devis



urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('propos/', propos, name='propos'),
    path('devis/', devis, name='devis'),
    ]
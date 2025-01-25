from django.urls import path
from wefix.views import index, contact, propos


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('propos/', propos, name='propos'),

    ]
    
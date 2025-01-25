from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def propos(request):
    return render(request, 'propos.html')
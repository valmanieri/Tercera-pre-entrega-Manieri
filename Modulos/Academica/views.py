from django.shortcuts import render
from django.conf import settings

# Create your views here.

def contacto (request):
    return render(request, "contacto.html")


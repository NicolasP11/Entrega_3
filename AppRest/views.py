from django.shortcuts import render
from AppRest.models import *

# Create your views here.

def inicio(request):
    return render(request, "AppRest/index.html")

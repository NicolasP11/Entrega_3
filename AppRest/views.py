from django.shortcuts import render
from AppRest.models import *
from AppRest.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):
    return render(request, "AppRest/index.html")

def buscar(request):

    if request.method == 'POST':

        miFormulario = BuscaProdForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            comidas = Comida.objects.filter(nombre__icontains=informacion["nombre"])
            return render(request, "AppRest/mostrarbusca.html", {"comidas": comidas})
    else:
        miFormulario = BuscaProdForm()

    return render(request, "AppRest/buscarprod.html", {"miFormulario": miFormulario})


def comidaForm(request):

    if request.method == 'POST':

        miFormulario = comidaFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            comida = Comida(nombre=informacion['nombre'], precio=informacion['precio'])
            comida.save()
            return render(request, "AppRest/index.html")
    else:
        miFormulario = comidaFormulario()

    return render(request, "AppRest/comida_form.html", {"miFormulario": miFormulario})



class CursoListView(ListView):

    model = Comida
    template_name = "AppRest/lista.html"

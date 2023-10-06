from django.urls import path
from AppRest import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('comidaform/', views.comidaForm, name="comida_form"),
    path('lista/', views.CursoListView.as_view(), name="List"),
    path('buscar/', views.buscar, name="Buscar"),
]
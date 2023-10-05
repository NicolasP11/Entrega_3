from django.urls import path
from AppRest import views

urlpatterns = [
    path('inicio/', views.inicio)
]
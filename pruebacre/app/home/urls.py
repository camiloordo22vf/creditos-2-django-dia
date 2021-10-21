from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('home/', views.PruebaView.as_view()),
    path('home2/', views.PruebaListView.as_view()),
    path('lista_peli/', views.Prueba_pListView.as_view()),
    path('agregar_p/', views.PruebaCreateView.as_view()),
]
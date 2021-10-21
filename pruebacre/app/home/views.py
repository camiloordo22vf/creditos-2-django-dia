from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .form import PruebaForm

class Prueba_pListView(ListView):
    template_name = 'home.html'
    model = Prueba
    context_object_name = 'lista_p'


class PruebaView(TemplateView):
    template_name = 'home.html'


class PruebaListView(ListView):
    template_name = "home.html"
    context_object_name = 'lista_n'
    queryset = ['camilo', 'alex','yuliana','David']


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home.html"
    form_class = PruebaForm
    success_url = "/success"




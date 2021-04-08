from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView




class PruebaView(TemplateView):
    template_name = 'home.html'


class PruebaListView(ListView):
    template_name = "home.html"
    context_object_name = 'lista_n'
    queryset = ['camilo', 'alex','yuliana','David']


    

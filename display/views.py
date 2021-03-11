from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Create your views here.
class DisplayPageView(TemplateView):
    template_name = "display.html"
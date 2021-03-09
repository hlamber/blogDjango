from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     return HttpResponse("""
#     <h1>Hello word !</h1>
#     <p>Ceci est ma première page avec django !</p>
#     """)

# class HomePageView(TemplateView):
#     template_name = "home/index.html"

def home(request):
    return render(request, 'home/index.html', {})

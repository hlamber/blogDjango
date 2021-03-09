from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     return HttpResponse("""
#     <h1>Hello word !</h1>
#     <p>Ceci est ma première page avec django !</p>
#     """)

<<<<<<< HEAD:home/views.py
# class HomePageView(TemplateView):
#     template_name = "home/index.html"

def home(request):
    return render(request, 'home/index.html', {})
=======
class HomePageView(TemplateView):
    template_name = "home/index.html"
>>>>>>> 2394ac2b8f032f81478daff64a8c1a9f73eeffb8:home/views.py

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return HttpResponse("""
#     <h1>Hello word !</h1>
#     <p>Ceci est ma première page avec django !</p>
#     """)

def home(request):
    return render(request, 'formation/accueil.html', {})

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView

# Create your views here.
# def home(request):
#     return HttpResponse(
#         """
#         <h1>Hello World</h1>
#         <p>Ceci est ma première page avec Django</p>
#         """
#     )

class AboutPageView(TemplateView):
    template_name = "about-us.html"

# def model(request):
#     return render(request, 'home/index.html')
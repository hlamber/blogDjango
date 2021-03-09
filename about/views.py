from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView # Import TemplateView

from .models import Contact
from .forms import ContactForm

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

class ContactPageView(TemplateView):
    template_name = "contact.html"

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False) 
            contact.username = request.username
            contact.mail = request.mail
            contact.message = request.message
            contact.date = timezone.now()
            contact.save()

    form = ContactForm()
    return render(request, 'contact.html', {'form': form })
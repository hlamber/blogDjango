from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView # Import TemplateView
from django.utils import timezone

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
    about = AboutPageView.as_view()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False) 
            # contact.username = request.username
            contact.username = form.cleaned_data['username']
            contact.mail = form.cleaned_data['mail']
            contact.message = form.cleaned_data['message']
            contact.date = timezone.now()
            contact.save()
            return redirect("https://wwww.askpython.com")
            # return redirect("../about/")
            # return redirect(request, 'about-us.html', {'form': form })
    form = ContactForm()
    return render(request, 'contact.html', {'form': form })

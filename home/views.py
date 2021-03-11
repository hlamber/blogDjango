from django.http import HttpResponse
from django.shortcuts import render

from .models import InfosPerso, Langue, Experience, Diplome, Skill
from .forms import InfosPersoForm, LangueForm, ExperienceForm, DiplomeForm, SkillForm

# Create your views here.
# def home(request):
#     return HttpResponse("""
#     <h1>Hello word !</h1>
#     <p>Ceci est ma première page avec django !</p>
#     """)

def home(request):
    return render(request, 'home/index.html', {})

def formCV(request):
    if request.method == "POST":
        infos = InfosPersoForm(request.POST)
        langue = LangueForm(request.POST)
        experience = ExperienceForm(request.POST)
        diplome = DiplomeForm(request.POST)
        skill = SkillForm(request.POST)
        if infos.is_valid() and langue.is_valid() and experience.is_valid() and diplome.is_valid() and skill.is_valid():
            infosPerso = infos.save(commit=False) 
            infosPerso.first_name = infos.cleaned_data['first_name']
            infosPerso.last_name = infos.cleaned_data['last_name']
            infosPerso.email = infos.cleaned_data['email']
            infosPerso.phone = infos.cleaned_data['phone']
            infosPerso.birthday = infos.cleaned_data['birthday']
            infosPerso.hobbies = infos.cleaned_data['hobbies']
            infosPerso.save()
            langueBdd = langue.save(commit=False) 
            # langueBdd.id_infosPerso = infosPerso.g
            # langueBdd.last_name = langue.cleaned_data['langue']
            # langueBdd.level = langue.cleaned_data['level']
            # langueBdd.save()
        return render(request, 'home/index.html')
    else:
        infos = InfosPersoForm()
        langue = LangueForm()
        experience = ExperienceForm()
        diplome = DiplomeForm()
        skill = SkillForm()
    return render(request, 'home/formCV.html', {'infos':infos, 'langue':langue, 'experience':experience, 'diplome':diplome, 'skill':skill})

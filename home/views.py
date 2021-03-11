from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView # Import TemplateView

from .models import InfosPerso, Langue, Experience, Diplome, Skill
from .forms import InfosPersoForm, LangueForm, ExperienceForm, DiplomeForm, SkillForm

class DisplayPageView(TemplateView):
    template_name = "home/display.html"

def display(request):
    infos = InfosPerso.objects.all().order_by('last_name')
    return render(request, 'home/display.html', {'infos': infos})

def cv_details(request, id):
    info = get_object_or_404(InfosPerso, pk=id)
    diplome = get_object_or_404(Diplome, id_infosPerso=id)
    experience = get_object_or_404(Experience, id_infosPerso=id)
    langues = get_object_or_404(Langue, id_infosPerso=id)
    skills = get_object_or_404(Skill, id_infosPerso=id)
    
    return render(request, 'home/cv_details.html', {'info': info, 'diplome' : diplome, 'experience': experience, 'langues' : langues, 'skills' : skills})
    # return render(request, 'home/cv_details.html', {'info': info})


def home(request):
    return render(request, 'home/index.html', {})

def formulaireCV(request):
    if request.method == "POST":
        infosPersoForm = InfosPersoForm(request.POST)
        langueForm = LangueForm(request.POST)
        experienceForm = ExperienceForm(request.POST)
        diplomeForm = DiplomeForm(request.POST)
        skillForm = SkillForm(request.POST)
        if infosPersoForm.is_valid() and langueForm.is_valid() and experienceForm.is_valid() and diplomeForm.is_valid() and skillForm.is_valid():
            print("Formulaire CV correct")
            infosPerso = infosPersoForm.save(commit=False) 
            infosPerso.first_name = infosPersoForm.cleaned_data['first_name']
            infosPerso.last_name = infosPersoForm.cleaned_data['last_name']
            infosPerso.email = infosPersoForm.cleaned_data['email']
            infosPerso.phone = infosPersoForm.cleaned_data['phone']
            infosPerso.birthday = infosPersoForm.cleaned_data['birthday']
            infosPerso.hobbies = infosPersoForm.cleaned_data['hobbies']
            infosPerso.save()
            
            langue = langueForm.save(commit=False) 
            langue.id_infosPerso = infosPerso
            langue.last_name = langueForm.cleaned_data['langue']
            langue.level = langueForm.cleaned_data['level']
            langue.save()

            experience = experienceForm.save(commit=False) 
            experience.id_infosPerso = infosPerso
            experience.experience_name = experienceForm.cleaned_data['experience_name']
            experience.start_date = experienceForm.cleaned_data['start_date']
            experience.end_date = experienceForm.cleaned_data['end_date']
            experience.description = experienceForm.cleaned_data['description']
            experience.save()

            diplome = diplomeForm.save(commit=False) 
            diplome.id_infosPerso = infosPerso
            diplome.degree_name = diplomeForm.cleaned_data['degree_name']
            diplome.mention = diplomeForm.cleaned_data['mention']
            diplome.institution = diplomeForm.cleaned_data['institution']
            diplome.obtained_years = diplomeForm.cleaned_data['obtained_years']
            diplome.save()

            skill = skillForm.save(commit=False) 
            skill.id_infosPerso = infosPerso
            skill.skill = skillForm.cleaned_data['skill']
            skill.level = skillForm.cleaned_data['level']
            skill.save()
            return render(request, 'home/index.html')
        else : 
            return render(request, 'home/formCV.html', {'infos':infosPersoForm, 'langue':langueForm, 'experience':experienceForm, 'diplome':diplomeForm, 'skill':skillForm})
    print("Formulaire CV incorrect")
    infos = InfosPersoForm()
    langue = LangueForm()
    experience = ExperienceForm()
    diplome = DiplomeForm()
    skill = SkillForm()
    return render(request, 'home/formCV.html', {'infos':infos, 'langue':langue, 'experience':experience, 'diplome':diplome, 'skill':skill})

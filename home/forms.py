from django import forms
from django.forms import widgets
from .models import InfosPerso, Langue, Experience, Diplome, Skill, MENTION_CHOICES, LEVEL_CHOICES
from django.forms.widgets import SelectDateWidget
from datetime import datetime

class InfosPersoForm(forms.ModelForm):
    birthday = forms.DateField(widget=SelectDateWidget(years=range(1960, datetime.now().year+1)))
    class Meta:
        model = InfosPerso
        fields = ('first_name', 'last_name', 'email','phone','birthday','hobbies')

class LangueForm(forms.ModelForm):
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Langue
        fields = ('langue', 'level')

class ExperienceForm(forms.ModelForm):
    start_date = forms.DateField(widget=SelectDateWidget(years=range(1960, datetime.now().year)))
    end_date = forms.DateField(widget=SelectDateWidget(years=range(1960, datetime.now().year + 10)))
    class Meta:
        model = Experience
        fields = ('experience_name', 'start_date', 'end_date', 'description')
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            print("date erreur")
            raise forms.ValidationError({"end_date": "La date ne peut être avant celle du début"})

def possible_years(first_year_in_scroll, last_year_in_scroll):
    p_year = []
    for i in range(first_year_in_scroll, last_year_in_scroll, -1):
        p_year_tuple = str(i), i
        p_year.append(p_year_tuple)
    return p_year

class DiplomeForm(forms.ModelForm):
    mention = forms.ChoiceField(choices=MENTION_CHOICES, widget=forms.RadioSelect())
    obtained_years = forms.ChoiceField(
    choices=possible_years(((datetime.now()).year), 1960)
)
    class Meta:
        model = Diplome
        fields = ('degree_name', 'mention', 'obtained_years', 'institution')
     

class SkillForm(forms.ModelForm):
    level = forms.ChoiceField(choices=LEVEL_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model = Skill
        fields = ('skill', 'level')
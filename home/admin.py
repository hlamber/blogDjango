from django.contrib import admin
from .models import InfosPerso, Langue, Experience, Diplome, Skill

admin.site.register(InfosPerso)
admin.site.register(Langue)
admin.site.register(Experience)
admin.site.register(Diplome)
admin.site.register(Skill)
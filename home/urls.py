from django.urls import path, re_path
from django.conf import settings

from . import views

urlpatterns = [ 
    path('', views.home, name='home'), 
    path('formulaireCV/', views.formulaireCV, name='formulaireCV'),
]
from django.conf.urls import url
from django.urls import path, re_path
from django.conf import settings

from . import views

urlpatterns = [ 
    path('', views.home, name='home'), 
    path('formulaireCV/', views.formulaireCV, name='formulaireCV'),
    path('display/', views.display, name='display'),
    path('cv_details/<int:id>/', views.cv_details, name='cv_details'),
]
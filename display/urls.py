# projetDjango/display/urls.py
from django.conf.urls import url
from display import views

urlpatterns = [
    url('display/', views.DisplayPageView.as_view(), name='display'),
]
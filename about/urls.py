# projetDjango/about/urls.py
from django.conf.urls import url
from about import views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url('about/', views.AboutPageView.as_view(), name='about'),
    url('contact/', views.ContactPageView.as_view(), name='contact'),
]
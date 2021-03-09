from django.conf.urls import url
from home import views
from django.conf.urls import url, include

urlpatterns = [
    url('', views.HomePageView.as_view(), name='home'),
]


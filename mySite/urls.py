from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include # Add include to the imports here

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('home.urls')),
    path('', include('django.contrib.auth.urls')),
    url(r'^', include('about.urls')), # tell django to read urls.py in example app
    url(r'^', include('display.urls')), # tell django to read urls.py in example app

]

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include # Add include to the imports here

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
<<<<<<< HEAD
    path('', include('home.urls')),
=======
    url(r'^', include('home.urls')),
>>>>>>> 2394ac2b8f032f81478daff64a8c1a9f73eeffb8
    path('', include('django.contrib.auth.urls')),
    url(r'^', include('about.urls')), # tell django to read urls.py in example app

]

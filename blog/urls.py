from django.urls import path, re_path
from django.conf import settings

from . import views

urlpatterns = [
    
    path('post', views.accueil, name='accueil'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post_add/', views.post_add, name='post_add'),
    path('post_add/<int:id>', views.post_add, name='post_add'),

]

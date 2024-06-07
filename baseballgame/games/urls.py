from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('soloPlay1/', views.soloPlay1, name="soloPlay1"),
    path('soloPlay2/', views.soloPlay2, name="soloPlay2"),
    path('multiPlay1/', views.multiPlay1, name="multiPlay1"),
    path('multiPlay1/', views.multiPlay1, name="multiPlay1"),
    path('test/', views.test, name="test"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]
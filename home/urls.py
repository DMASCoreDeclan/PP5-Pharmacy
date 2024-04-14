from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('healthcare_advice/', views.healthcare_advice, name='healthcare_advice'),
    path('healthcare_advice/add/', views.add_web_article, name='add_web_article'),
]

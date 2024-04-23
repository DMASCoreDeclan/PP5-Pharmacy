from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('healthcare_advice/', views.healthcare_advice, name='healthcare_advice'),
    path('healthcare_advice/add/', views.add_article, name='add_article'),
    path('healthcare_advice/edit/<slug:slug>/<int:article_id>', views.edit_article, name='edit_article'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

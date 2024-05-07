from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all_articles/', views.all_articles, name='all_articles'),
    path('all_articles/add/', views.add_article, name='add_article'),
    path('all_articles/edit/<slug:slug>/<int:article_id>', views.edit_article, name='edit_article'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

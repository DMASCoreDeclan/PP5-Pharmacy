from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all_articles/', views.all_articles, name='all_articles'),
    path('add/', views.add_article, name='add_article'),
    path('edit/', views.edit_articles, name='edit_articles'),
    path('edit/<slug:slug>', views.edit_article, name='edit_article'),
    path('<int:article_id>', views.article_detail, name='article_detail'),
    path('delete_articles/', views.delete_articles, name='delete_articles'),
    path('delete_article/<slug:slug>', views.delete_article, name='delete_article'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

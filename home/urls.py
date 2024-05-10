from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all_articles/', views.all_articles, name='all_articles'),
    path('all_services/', views.all_services, name='all_services'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_service/', views.add_service, name='add_service'),
    path('edit_article/', views.edit_articles, name='edit_articles'),
    path('edit_services/', views.edit_services, name='edit_services'),
    path('edit_article/<slug:slug>', views.edit_article, name='edit_article'),
    path(
        'edit_service/<int:service_id>',
        views.edit_service,
        name='edit_service'
        ),
    path(
        'article_detail/<int:article_id>',
        views.article_detail,
        name='article_detail'
        ),
    path(
        'service_detail/<int:service_id>',
        views.service_detail,
        name='service_detail'
        ),
    path('delete_articles/', views.delete_articles, name='delete_articles'),
    path('delete_services/', views.delete_services, name='delete_services'),
    path(
        'delete_article/<slug:slug>',
        views.delete_article,
        name='delete_article'
        ),
    path(
        'delete_service/<int:service_id>',
        views.delete_service,
        name='delete_service'
        ),
    path('subscribe/', views.subscribe, name='subscribe'),
]

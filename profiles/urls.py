from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
        ),
    path(
        'px_order_history/<px_order_number>',
        views.px_order_history,
        name='px_order_history'
        ),
]

from django.urls import path

from . import views


name_app = 'orders'
urlpatterns = [
    path('create/', views.order_create_view, name='order_create'),
]

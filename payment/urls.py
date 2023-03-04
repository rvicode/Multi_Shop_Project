from django.urls import path

from . import views


urlpatterns = [
    path('process/', views.payment_process, name='payment_process'),
    path('callback/', views.payment_callback, name='payment_callback'),
]

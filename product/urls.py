from django.urls import path

from . import views


app_name = "product"
urlpatterns = [
    path('detail/<int:pk>', views.product_detail_view, name='product_detail'),
    path("list/<int:pk>", views.product_list_view, name='product_list'),
]

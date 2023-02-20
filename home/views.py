from django.shortcuts import render

from product.models import Product, Category


def home_view(request):
    products = Product.objects.all()
    category = Category.objects.all()[:12]

    return render(request, 'home/home.html', {'products': products, 'category': category})

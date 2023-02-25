from django.shortcuts import render
# from django.views.decorators.cache import cache_page

from product.models import Product, Category


# @cache_page(60 * 1)       # Just For Test
def home_view(request):
    products = Product.objects.all()
    category = Category.objects.all()[:12]

    return render(request, 'home/home.html', {'products': products, 'category': category})

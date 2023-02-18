from django.shortcuts import render, get_object_or_404

from .models import Product


def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    product_list = Product.objects.all()
    return render(request, 'product/product_detail.html', {'product': product, 'product_list': product_list})

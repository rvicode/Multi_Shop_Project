from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .cart import Cart
from product.models import Product
from .forms import ProductCartForm


@require_GET
def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = ProductCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = ProductCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_detail')


def remove_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

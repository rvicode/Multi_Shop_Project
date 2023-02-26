from django.shortcuts import render
from django.views.decorators.http import require_GET

from .cart import Cart
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

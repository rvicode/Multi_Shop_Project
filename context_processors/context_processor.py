from cart.cart import Cart


def cart_detail_view(request):
    return {'cart': Cart(request)}
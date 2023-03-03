from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart


@login_required
def order_create_view(request):
    form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _('Your Cart Is empty!'))
        return redirect('product:product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)
            order_obj.username = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price,
                )

            cart.clear()

            request.user.first_name = order_obj.firstname
            request.user.last_name = order_obj.lastname
            request.user.save()

            request.session['order_id'] = order_obj.id
            return redirect('payment:payment_process')

    return render(request, 'orders/checkout.html', {'form': form})

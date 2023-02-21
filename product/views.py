from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import Product, Comment
from .forms import CommentForm


def product_detail_view(request, pk):

    product = get_object_or_404(Product, id=pk)
    product_list = Product.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            username = request.user
            product_id = product
            message = form.cleaned_data.get("massage")

            if username and product_id and message:
                Comment.objects.create(username=username, product=product_id, massage=message)
                messages.success(request, _("The Comment Was Sent"))
                return redirect(reverse('product:product_detail', args=[str(product.id)]))

        else:
            return messages.error(request, _("Please check your form!"))

    else:
        form = CommentForm()
    return render(request, 'product/product_detail.html',
                  {'product': product, 'product_list': product_list, 'form': form})

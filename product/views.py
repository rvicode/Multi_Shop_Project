from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.views import generic

from .models import Product, Comment
from .forms import CommentForm


def product_detail_view(request, pk):

    product = get_object_or_404(Product, id=pk)
    product_list = Product.objects.all()[:5]

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            username = request.user
            product_id = product
            message = form.cleaned_data.get("massage")
            score = form.cleaned_data.get("score")

            if username and product_id and message:
                Comment.objects.create(username=username, product=product_id, score=score, massage=message)
                messages.success(request, _("The Comment Was Sent"))
                return redirect(reverse('product:product_detail', args=[str(product.id)]))

        else:
            return messages.error(request, _("Please check your form!"))

    else:
        form = CommentForm()
    return render(request, 'product/product_detail.html',
                  {'product': product, 'product_list': product_list, 'form': form})


class ProductListView(generic.ListView):
    model = Product
    template_name = "product/all_product.html"
    context_object_name = "product"
    paginate_by = 12

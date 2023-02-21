from django.shortcuts import render, get_object_or_404, HttpResponse

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
                return render(request, 'product/product_detail.html', {'product': product})

        else:
            return HttpResponse("Error")

    else:
        form = CommentForm()
    return render(request, 'product/product_detail.html',
                  {'product': product, 'product_list': product_list, 'form': form})

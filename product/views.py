from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from .models import Product, Comment, Category
from .forms import CommentForm


def product_detail_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    product_list = Product.objects.all().order_by("-datetime_created")[:5]

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


def product_list_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    product = Product.objects.filter(category=category)
    paginator = Paginator(product, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/all_product.html', {"product_list": page_obj})


def product_search_list_view(request):
    q = request.GET.get("q")
    product = Product.objects.filter(Q(name_product=q) | Q(short_description=q))
    paginator = Paginator(product, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/all_product.html', {"product_list": page_obj})

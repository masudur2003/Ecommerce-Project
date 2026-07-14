from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from shop.models import Product


@login_required
def wishlist(request):

    items = Wishlist.objects.filter(
        user=request.user
    )

    return render(
        request,
        "wishlist.html",
        {"items": items}
    )


@login_required
def add_wishlist(request, id):

    product = get_object_or_404(Product, id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        product=product
    )

    return redirect(request.META.get("HTTP_REFERER"))


@login_required
def remove_wishlist(request, id):

    product = get_object_or_404(Product, id=id)

    Wishlist.objects.filter(
        user=request.user,
        product=product
    ).delete()

    return redirect("wishlist")
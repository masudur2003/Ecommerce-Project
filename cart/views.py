from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart')


def cart(request):
    cart = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            continue

        product.quantity = quantity
        product.total_price = product.price * quantity

        total += product.total_price
        products.append(product)

    context = {
        'products': products,
        'total': total,
    }

    return render(request, 'cart.html', context)


def increase_quantity(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart')


def decrease_quantity(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart')


def checkout(request):

    ids = request.POST.getlist('selected_products')

    cart = request.session.get('cart', {})

    products = []
    total = 0

    for product_id in ids:

        if product_id in cart:

            product = get_object_or_404(Product, id=product_id)

            product.quantity = cart[product_id]
            product.total_price = product.price * cart[product_id]

            total += product.total_price
            products.append(product)


    return render(request, 'checkout.html', {
        'products': products,
        'total': total
    })
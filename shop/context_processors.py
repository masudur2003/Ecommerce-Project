from .models import Category
from wishlist.models import Wishlist

def categories(request):
    return {
        "categories": Category.objects.all()
    }


# Cart context processor

def cart_count(request):
    cart = request.session.get('cart', {})

    return {
        'cart_count': sum(cart.values())
    }





# Wishlist context processor

def wishlist_count(request):

    if request.user.is_authenticated:

        count = Wishlist.objects.filter(
            user=request.user
        ).count()

    else:
        count = 0

    return {
        "wishlist_count": count
    }
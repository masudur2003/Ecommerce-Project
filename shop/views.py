from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Contact
from shop.models import Product, Category



def home(request):

    products = Product.objects.all()

    return render(
        request,
        "home.html",
        {
            "products": products
        }
    )



def about(request):
    return render(request, "about.html")



def services(request):
    return render(request, "services.html")



def contact(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")


        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            message=message
        )


    return render(request, "contact.html")



def product_details(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        "product_details.html",
        {
            "product": product
        }
    )



def category_products(request, slug):

    category = get_object_or_404(
        Category,
        slug=slug
    )

    products = Product.objects.filter(
        category=category
    )


    return render(
        request,
        "category_products.html",
        {
            "category": category,
            "products": products
        }
    )



def search(request):

    query = request.GET.get('q')

    products = Product.objects.none()


    if query:

        products = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )


    return render(
        request,
        "search_results.html",
        {
            "products": products,
            "query": query
        }
    )
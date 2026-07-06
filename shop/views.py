from django.shortcuts import render
from .models import Contact
from shop.models import Product

def home(request):
    products = Product.objects.all()

    return render(request, "home.html", {
        "products": products
    })

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


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
            message=message,
        )
        print("Data Saved Successfully")
    return render(request, "contact.html")


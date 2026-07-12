from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("shop:home")

        return render(request, "login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("shop:home")




def register_view(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")


        if password != confirm_password:

            return render(request, "register.html", {
                "error": "Password does not match!"
            })


        if User.objects.filter(username=username).exists():

            return render(request, "register.html", {
                "error": "Username already exists!"
            })


        if User.objects.filter(email=email).exists():

            return render(request, "register.html", {
                "error": "Email already exists!"
            })


        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )


        user.save()


        return redirect("user_accounts:login")


    return render(request, "register.html")
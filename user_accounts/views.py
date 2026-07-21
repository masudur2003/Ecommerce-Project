from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import UserProfile
from .forms import UserForm, ProfileForm



# =========================
# Login View
# =========================

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


            # Create profile if not exists
            UserProfile.objects.get_or_create(
                user=user
            )


            messages.success(
                request,
                "Login successful"
            )


            return redirect(
                "shop:home"
            )


        else:

            messages.error(
                request,
                "Invalid username or password"
            )



    return render(
        request,
        "login.html"
    )





# =========================
# Logout View
# =========================

@login_required
def logout_view(request):

    logout(request)


    messages.success(
        request,
        "Logout successful"
    )


    return redirect(
        "shop:home"
    )





# =========================
# Register View
# =========================

def register_view(request):


    if request.method == "POST":


        first_name = request.POST.get(
            "first_name"
        )

        last_name = request.POST.get(
            "last_name"
        )

        username = request.POST.get(
            "username"
        )

        email = request.POST.get(
            "email"
        )

        password = request.POST.get(
            "password"
        )

        confirm_password = request.POST.get(
            "confirm_password"
        )



        if password != confirm_password:

            messages.error(
                request,
                "Password does not match"
            )

            return redirect(
                "user_accounts:register"
            )



        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists"
            )

            return redirect(
                "user_accounts:register"
            )



        if User.objects.filter(
            email=email
        ).exists():

            messages.error(
                request,
                "Email already exists"
            )

            return redirect(
                "user_accounts:register"
            )



        user = User.objects.create_user(

            username=username,

            email=email,

            password=password,

            first_name=first_name,

            last_name=last_name

        )


        # create profile

        UserProfile.objects.get_or_create(
            user=user
        )



        messages.success(
            request,
            "Registration successful"
        )


        return redirect(
            "user_accounts:login"
        )



    return render(
        request,
        "register.html"
    )







# =========================
# Dashboard
# =========================

@login_required
def dashboard(request):


    UserProfile.objects.get_or_create(
        user=request.user
    )


    return render(
        request,
        "dashboard.html"
    )







# =========================
# Profile
# =========================

@login_required
def profile(request):


    UserProfile.objects.get_or_create(
        user=request.user
    )


    return render(
        request,
        "profile.html"
    )







# =========================
# Edit Profile
# =========================

@login_required
def edit_profile(request):


    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )



    if request.method == "POST":


        user_form = UserForm(

            request.POST,

            instance=request.user

        )



        profile_form = ProfileForm(

            request.POST,

            request.FILES,

            instance=profile

        )




        if user_form.is_valid() and profile_form.is_valid():


            user_form.save()

            profile_form.save()



            messages.success(
                request,
                "Profile updated successfully"
            )


            return redirect(
                "user_accounts:profile"
            )



    else:



        user_form = UserForm(
            instance=request.user
        )


        profile_form = ProfileForm(
            instance=profile
        )




    context = {

        "user_form": user_form,

        "profile_form": profile_form

    }




    return render(

        request,

        "edit_profile.html",

        context

    )
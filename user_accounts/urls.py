from django.urls import path

from . import views

app_name = "user_accounts"

urlpatterns = [
    # Authentication
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # User Profile
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]
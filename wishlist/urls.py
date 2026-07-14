from django.urls import path
from . import views

urlpatterns = [

    path("", views.wishlist, name="wishlist"),

    path("add/<int:id>/",
         views.add_wishlist,
         name="add_wishlist"),

    path("remove/<int:id>/",
         views.remove_wishlist,
         name="remove_wishlist"),

]
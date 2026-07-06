from django.contrib import admin
from .models import Contact
from .models import Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "message",
        "created_at",
    ]
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
        "description",
        "image",
        "stock",
    ]
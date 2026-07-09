from django.contrib import admin
from .models import Contact
from .models import Product, Category


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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
 
    
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

    





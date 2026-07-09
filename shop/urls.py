
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:id>/',views.product_details,name='product_details'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    ]
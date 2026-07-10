from django.contrib import admin
from django.urls import path, include
from ecommerce_project import settings

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("shop.urls", "shop"), namespace="shop")),
    path('', include(('cart.urls', 'cart'), namespace='cart')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

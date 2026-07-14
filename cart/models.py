from django.db import models
from django.contrib.auth.models import User
from shop.models import Product



class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )


    is_selected = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def total_price(self):

        return self.product.price * self.quantity



    def __str__(self):

        return self.user.username
from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | {self.message}"

    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.URLField()  
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
         return f"{self.name} | {self.price} | {self.description} | {self.image} | {self.stock}"




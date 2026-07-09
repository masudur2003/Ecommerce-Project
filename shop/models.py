from django.db import models

# Contact Model
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone} | {self.email} | {self.message}"



# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
    

    # Product Model Update
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True, blank=True)

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.price} | {self.description} | {self.image} | {self.stock}"






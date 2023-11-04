from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-generated ID field
    name = models.CharField(max_length=255)  # Name of the product
    description = models.TextField()  # Description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    image = models.FileField(blank=False, upload_to="productimages")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who added the product to the cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Product added to the cart
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the product in the cart

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

from django.db import models
from django.contrib import admin

class Product(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
    @admin.display(
        boolean=True,
        ordering="id",
        description="Product ID",
    )

    def is_stock_available(self):
        return self.stock > 0
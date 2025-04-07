from django.db import models
from django.contrib import admin

class Product(models.Model):
    product_id = models.CharField(max_length=200)
    product_name = models.CharField(max_length=500)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock = models.IntegerField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name
    
    @admin.display(
        boolean=True,
        ordering="id",
        description="Product ID",
    )

    def is_stock_available(self):
        return self.product_stock > 0
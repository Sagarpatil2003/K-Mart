from django.db import models
from django.contrib.auth.models import User
from product.models import Product, ProductVariation


class Order(models.Model):
    STATUS_CHOICE = (
        # Key       Value
        ('Pending', 'Pending'),
        ('Inprogress', 'Inprogress'),
        ('Dispatch', 'Dispatch'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
        ('Rejected', 'Rejected'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    address = models.TextField()
    mobile = models.CharField(max_length=12)
    payment = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    variation = models.ForeignKey(ProductVariation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.order.id} {self.product.name}"

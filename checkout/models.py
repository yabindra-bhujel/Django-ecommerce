from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from shop.models import Product


from django.db import models


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank= True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=50,blank= True, null=True)
    
    def __str__(self):
        return self.full_name


class Order(models.Model):
    ORDERED = 'Ordered'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered')
    )

    product = models.ForeignKey(
        Product, related_name='items', on_delete=models.CASCADE, null=True)
    order_no = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='orders',
                             on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    status = models.CharField(
        max_length=30, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order {self.order_no}'

    def get_absolute_url(self):
        return reverse('order', args=[self.id])




class OrderItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE )

    def __str__(self):
        return f"{self.quantity} of {self.products.title}"

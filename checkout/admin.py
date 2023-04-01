
from django.contrib import admin
from .models import Order, OrderItem, Customer

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)

# Register your models here.

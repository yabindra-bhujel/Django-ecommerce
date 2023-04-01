from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)



class ProductAdmin(admin.AdminSite):
    site_header = 'Product Administration'
    
    
product_admin_site = ProductAdmin(name='product_admin')
product_admin_site.register(Product)

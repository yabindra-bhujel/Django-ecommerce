from django.apps import apps
from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Customer


class AdminOrderItem(admin.ModelAdmin):
    list_display = ['user', 'products','price','order']
admin.site.register(OrderItem, AdminOrderItem)


class AdminOrder(admin.ModelAdmin):
    pass
admin.site.register(Order, AdminOrder)


class AdminCustomer(admin.ModelAdmin):
    pass
admin.site.register(Customer, AdminCustomer)

class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'discptrion']

admin.site.register(Category, AdminCategory)



class AdminProduct(admin.ModelAdmin):
    pass
admin.site.register(Product, AdminProduct)



#  new pages for staff
class ProductAdmin(admin.AdminSite):
    site_header = ' Staff Pages'
    

class TestAdminPermission(admin.ModelAdmin):
    
    def has_add_permission(self, request, obj = None):
        return True
    
    
    def has_change_permission(self, request, obj = None):
        return True
    
    def has_delete_permission(self, request, obj = None):
        return True
    
    
    def has_view_permission(self, request, obj = None):
        return True
    

product_admin_site = ProductAdmin(name='product_admin')
product_admin_site.register(Category, AdminCategory)
product_admin_site.register(Product, AdminProduct)
product_admin_site.register(Customer, AdminProduct)
product_admin_site.register(Order, AdminProduct)
product_admin_site.register(OrderItem, AdminProduct)

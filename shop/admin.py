from django.apps import apps
from django.contrib import admin
from .models import Product, Category, Order, OrderItem, Customer


class AdminOrderItem(admin.ModelAdmin):
    list_display = ['user', 'price', 'order', 'quantity']
admin.site.register(OrderItem, AdminOrderItem)


class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'paid', 'status', 'customer']
    list_filter = ['status']
admin.site.register(Order, AdminOrder)


class AdminCustomer(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'phone', 'postal_code']
admin.site.register(Customer, AdminCustomer)

class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'discptrion']
admin.site.register(Category, AdminCategory)



class AdminProduct(admin.ModelAdmin):
     list_display = ['title', 'user', 'price',
                    'category', 'is_stock', 'product_code']
     list_filter = ['is_stock',  'is_discountable', 'is_public']
admin.site.register(Product, AdminProduct)



#  new pages for staff
class StaffAdminsite(admin.AdminSite):
    site_header = ' Staff Pages'
    
    
class CategoryStaffAdminPermission(admin.ModelAdmin):
    list_display = ['name', 'discptrion']

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    
    
class ProductStaffAdminPermission(admin.ModelAdmin):
    list_display = ['title', 'user', 'price',
                    'category', 'is_stock', 'product_code']
    list_filter = ['is_stock',  'is_discountable', 'is_public']

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    


class CustomerStaffAdminPermission(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'phone', 'postal_code']
    list_filter = ['is_active']
    
    
    def has_add_permission(self, request, obj = None):
        return False
    
    
    def has_change_permission(self, request, obj = None):
        return False
    
    def has_delete_permission(self, request, obj = None):
        return False
    
    
    def has_view_permission(self, request, obj = None):
        return True


class OrderStaffAdminPermission(admin.ModelAdmin):
    list_display = ['user', 'paid', 'status','customer']
    list_filter = ['status']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True


class OrderItemStaffAdminPermission(admin.ModelAdmin):
    list_display = ['user', 'quantity', 'price']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True



product_admin_site = StaffAdminsite(name='product_admin')

product_admin_site.register(Category, CategoryStaffAdminPermission)

product_admin_site.register(Product, ProductStaffAdminPermission)

product_admin_site.register(Customer, CustomerStaffAdminPermission)

product_admin_site.register(Order, OrderStaffAdminPermission)

product_admin_site.register(OrderItem, OrderItemStaffAdminPermission)

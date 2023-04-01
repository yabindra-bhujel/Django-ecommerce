from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.product_list, name='product_list'),
    path('product_detail/<int:id>/', views.productDetail, name='product_detail'),
    path('cart', views.CartItem, name='cart'),
    path('productCategor', views.productCategor, name='productCategor'),
    path('allProduct/', views.allProduct, name='allProduct'),
    path('category/<category>/', views.category_list, name='category'),
    path('categoryBase/', views.categoryBase, name='categoryBase'),
]

handler404 = 'shop.views.pageNotFound'

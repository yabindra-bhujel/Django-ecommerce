from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from shop.cart import Cart
from shop.forms import AddtoCartForm
from shop.models import Product, Category


def base(request):
    cart = Cart(request)
    return render(request, 'shop/base.html', {'cart': cart})


def categoryBase(request):
    category_list = Category.objects.all()
    return render(request, 'shop/categoryBase.html', {'category_list': category_list})



def product_list(request):
    queryset = Product.objects.all().order_by(
        '-posted_at')[:100]
    context = {
        "object_list": queryset,
    }
    return render(request, 'shop/product_list.html', context)






def productDetail(request, id):
    cart = Cart(request)
    obj = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = AddtoCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=id,
                     quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

    else:
        form = AddtoCartForm()

    related_products = Product.objects.filter(
        category=obj.category).exclude(id=id)[:50]
    context = {
        "related_products": related_products,
        "object": obj,
        'cart': cart,
    }
    return render(request, 'shop/product_detail.html', context)






@login_required(login_url="/login")
def CartItem(request):
    producst = Product.objects.all()
    cart_item = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart_item.remove(remove_from_cart)

        return redirect('cart')

    if change_quantity:
        cart_item.add(change_quantity, quantity, True)

        return redirect('cart')
    else:
        return render(request, 'shop/cart.html', {'cart_item': cart_item,
                                               })



def allProduct(request):
    queryset = Product.objects.all().order_by('-posted_at')
    category_list = Category.objects.all()
    context = {
        "queryset": queryset,
        "category_list": category_list,
    }

    return render(request, 'shop/allProducts.html' , context)


def category_list(request, category=None):
    current_category = category
    if category:
        products = Product.objects.filter(category__name=category)
    else:
        products = Product.objects.all()
    category_list = Category.objects.exclude(name='default')
    ct = Category.objects.all()
    context = {
        'cat': category,
        'products': products,
        'ct': ct,
        'category_list': category_list,
        'current_category': current_category,
    }
    return render(request, 'shop/category.html', context)


def productCategor(request):
    return render(request, 'shop/category.html')

def pageNotFound(request, exception):
    return render(request, 'shop/404.html')
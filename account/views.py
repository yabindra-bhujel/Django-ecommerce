from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Customer
from checkout.forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from checkout.models import Order, OrderItem




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'account/login.html')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            customer = Customer.objects.create(
                user=user,
                full_name = full_name,
                email = email,
            )
            customer.save()
            return redirect('login')
        else:
            messages.error(request, form.errors)
            return redirect('register')
    else:
        form = UserRegisterForm()
        return render(request, 'account/singup.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('product_list')




@login_required(login_url='account/login')
def customerProfile(request, id):
    user = User.objects.get(id=request.user.id)
    customer = get_object_or_404(Customer, id = id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    
    if request.method == 'POST':
        passwordChange= PasswordChangeForm(user=request.user, data = request.POST)
        if passwordChange.is_valid():
            user = authenticate(username = request.user.username, password = passwordChange.cleaned_data['old_password'])
            if user is not None:
                user.set_password(passwordChange.cleaned_data['new_password1'])
                user.save()
                login(request, user)
                return redirect('product_list')
            else:
                messages.error(request, passwordChange.errors)
                return redirect('profile')
    else:
        form = CustomerForm(instance=customer)
        passwordChange = PasswordChangeForm(user==request.user)
        context = {
            'form': form,
            'customer': customer,
            'user': user,
            'passwordChange': passwordChange,
        }
        return render(request, 'account/profile.html', context)
    
    return render(request, 'account/profile.html')




def userOrder(request):
    order = Order.objects.all()
    orderitem = OrderItem.objects.all()
    
    context = {
        'order': order,
        'orderitem': orderitem,
    }
    return render(request, 'account/order.html', context)
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import stripe
from django.contrib.auth.models import User
from django.db import transaction


from checkout.forms import CustomerForm
from shop.models import Order, OrderItem, Customer, Product
from shop.cart import Cart


# Create your views here.

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    customer = Customer.objects.filter(user=request.user).first()
    cart = Cart(request)

    if request.method == 'GET':
        domain_url = 'http://127.0.0.1:8000'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            line_items = []
            for item in cart:
                line_item = {
                    'price_data': {
                        'currency': 'jpy',
                        'product_data': {
                            'name': item['product'].title,
                        },
                        'unit_amount': int(item['product'].price),
                    },
                    'quantity': item['quantity'],
                }
                line_items.append(line_item)
                metadata = {
                    'user_id': request.user.id,
                    'user_email': request.user.email,
                    'user_name': request.user.username,
                    'customer_id': customer.id,
                    'customer_name': customer.full_name,
                    'customer_email': customer.email,
                    'customer_address_2': customer.address_line_1,
                    'customer_address_2': customer.address_line_2,
                    'customer_city': customer.city,
                    'customer_state': customer.state,
                    'customer_country': customer.postal_code,
                    'customer_zip': customer.phone,
                    'products': item['product'].title,
                    'products_id': item['product'].id,
                    'products_quantity': item['quantity'],
                    'products_price': item['product'].price,
                    

                }

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url='http://127.0.0.1:8000/success',
                cancel_url='http://127.0.0.1:8000/cancel',
                metadata=metadata,

            )
            print(session)
            return JsonResponse({'sessionId': session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def success(request):
    return render(request, 'checkout/success.html')


def cancel(request):
    return render(request, 'checkout/cancle.html')


@csrf_exempt
def stripe_webhook(request):
    cart = Cart(request)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    sig_header = request.headers['Stripe-Signature']

    try:
        event = stripe.Webhook.construct_event(
            request.body, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return JsonResponse({'success': False}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return JsonResponse({'success': False}, status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        metadata = event['data']['object']['metadata']

        order = Order.objects.create(
            order_no=event['data']['object']['id'],
            status='Ordered',
            paid=True,
            user_id=metadata['user_id'],
            customer_id=metadata['customer_id'],
            product_id=metadata['products_id'],
        )
        product = Product.objects.get(id=int(metadata['products_id']))
        order_item = OrderItem.objects.create(
            product=product,
            user_id =metadata['user_id'],
            order = order,
            quantity=metadata['products_quantity'],
            price=metadata['products_price'],

        )
        order.save()
        order_item.save()
        cart.clear()

    else:

        print('Unhandled event type {}'.format(event['type']))
    return HttpResponse(status=200)


def checkout(request, id):

    products = Product.objects.all()
    cart = Cart(request)
    customer = get_object_or_404(Customer, id=id)
    user = request.user

    cart = Cart(request)

    session_id = request.GET.get('session_id')
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)

        # If the session has been completed, create an order
        if session['payment_status'] == 'paid':
            order = Order.objects.get(order_no=session['id'])
            order.status = 'Ordered'
            order.paid = True
            order.user = user
            order.product = cart.cart.items
            order.save()

            # Clear the cart
            cart.clear()

    context = {'customer': customer, 'cart_items': cart}

    return render(request, 'checkout/checkout.html', context)

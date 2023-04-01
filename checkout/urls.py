from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.stripe_config, name='stripe_config'),
    path('create-checkout-session/', views.create_checkout_session,
         name='create_checkout_session'),
    path('checkout/ <int:id>', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    path('webhook', views.stripe_webhook, name="webhook")
]

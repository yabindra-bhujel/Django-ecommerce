from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import stripe

from django.conf import settings
stripe.api_key = settings. STRIPE_SECRET_KEY


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    discptrion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.id])


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    product_code_number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    is_discountable = models.BooleanField(default=True)
    first_images = models.ImageField()
    second_images = models.ImageField()
    third_images = models.ImageField()
    forth_images = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    price = models.BigIntegerField()
    is_stock = models.BooleanField(default=True)
    stripe_product_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_price_id = models.CharField(max_length=220, blank=True, null=True)
    stripe_price = models.IntegerField(default=1000)
    
    
 
    def save(self, *args, **kwargs):
        if self.title:
            stripe_product_name = stripe.Product.create(name=self.title)
            self.stripe_product_id = stripe_product_name.id
        if not self.stripe_price_id:
            stripe_price_obj = stripe.Price.create(
                product=self.stripe_product_id,
                unit_amount=self.stripe_price,
                currency="jpy"
            )
            self.stripe_price_id = stripe_price_obj.id
            if self.stripe_product_id:
                stripe_price_obj = stripe.Price.create(
                    product=self.stripe_product_id,
                    unit_amount=self.stripe_price,
                    currency="jpy"
                )
                self.stripe_price_id = stripe_price_obj.id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self, ):
        return reverse("product_detail", args=[self.id])


  
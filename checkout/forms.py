from django import forms

from shop.models import Order, Customer




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'address_line_1',
            'address_line_2', 'city', 'state', 'postal_code', 'phone']

from django import forms
class AddtoCartForm(forms.Form):
    quantity = forms.IntegerField()
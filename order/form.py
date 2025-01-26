from django import forms
from .models import Order

class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name','date','amount','price','description','payed']

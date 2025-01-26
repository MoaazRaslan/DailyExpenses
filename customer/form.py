from django import forms
from .models import Customer

class CustomerCreateForm(forms.ModelForm):

    class Meta:
        model =Customer
        fields=['name','phone_number','description','user','address']

    def clean(self):
        cleaned_data= super().clean()
        customer_name = cleaned_data.get('name')
        user = cleaned_data.get('user')
 
        if Customer.objects.filter(user = user,name = customer_name).exists():
            raise ValueError('Customer with this User already exists.!!')
        print('cleanign data')
        print(cleaned_data)
        return cleaned_data
    
class CustomerUpdateForm(forms.ModelForm):

    class Meta:
        model =Customer
        fields=['name','phone_number','description','address']

    def clean(self):
        cleaned_data= super().clean()
        customer_name = cleaned_data.get('name')
        user = cleaned_data.get('user')
 
        if Customer.objects.filter(user = user,name = customer_name).exists():
            raise ValueError('Customer with this User already exists.!!')
        print('cleanign data')
        print(cleaned_data)
        return cleaned_data
    

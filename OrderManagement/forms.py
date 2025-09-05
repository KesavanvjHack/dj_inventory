# from django.forms import ModelForm
from django import forms

from .models import *

class Customer_Form(forms.ModelForm):

    class Meta:

        model = Customer
        fields = '__all__'
        
        
        widgets = {
            
            'customer_name' : forms.TextInput(attrs={'class' : "form-control"}),
            'customer_id' : forms.TextInput(attrs={'class' : "form-control"}),
            'customer_email' : forms.EmailInput(attrs={'class' : "form-control"}),
            'customer_country' : forms.TextInput(attrs={'class' : "form-control"}),
            'customer_joined' : forms.DateTimeInput(attrs={'class' : "form-control"}),

            'picture' : forms.FileInput(attrs={'class' : "form-control"}),
        }
        
        
        
class Order_Form(forms.ModelForm):

    class Meta:

        model = Order
        fields = ['customer_reference','product_reference','order_number','order_date','quantity']
        
        
        widgets = {
            
            'customer_reference' : forms.Select(attrs={'class' : "form-control"}),
            'product_reference' : forms.Select(attrs={'class' : "form-control"}),
            'order_number' : forms.TextInput(attrs={'class' : "form-control"}),
            'order_date' : forms.DateInput(attrs={'class' : "form-control"}),
            'quantity' : forms.NumberInput(attrs={'class' : "form-control"}),
            
        }
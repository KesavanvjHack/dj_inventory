from django.db import models

from Inventory.models import *

class Customer(models.Model):

    customer_name = models.CharField(max_length=100, null=True)
    customer_id = models.CharField(max_length=50, unique=True, null=True)
    customer_email = models.EmailField(max_length=100, null=True)
    customer_country = models.CharField(max_length=50, null=True)
    customer_joined = models.DateTimeField(auto_now_add=True)
    
    picture = models.ImageField(null = True, blank = True, upload_to = 'customers/')


    def __str__(self): #type: ignore

        return self.customer_name 



class Order(models.Model):

    customer_reference = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    product_reference = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    order_number = models.CharField(max_length=20, null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)



    def __str__(self): # type: ignore

        return self.order_number
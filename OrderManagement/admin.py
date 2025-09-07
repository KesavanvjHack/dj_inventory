from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','customer_name','customer_id','customer_email','customer_country','customer_joined','picture')
    search_fields = ('id','customer_name','customer_id')
    ordering = ['id']
    
admin.site.register(Customer,CustomerAdmin)
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','customer_reference','product_reference','order_number','order_date','quantity','amount','gst_amount','bill_amount')
    search_fields = ('id','order_number')
    ordering = ['id']


admin.site.register(Order,OrderAdmin)
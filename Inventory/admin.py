from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name','product_code','price','gst','food_product','picture' )
    search_fields = ('id','product_name','product_code')
    ordering = ['id']


admin.site.register(Product, ProductAdmin)

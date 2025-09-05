from django.urls import path

from .views import *

urlpatterns = [
    path('customers/add/', CustomersAdd),
    path('customers/', AllCustomers),
    path('customers/delete/<int:id>/', DeleteCustomers, name='customer_delete'),
    path('customers/update/<int:id>/', UpdateCustomers, name='customer_update'),
    
    path('orders/add/', OrdersAdd),
    path('orders/', AllOrders),
    path('orders/delete/<int:id>/', DeleteOrders, name='order_delete'),
    path('orders/update/<int:id>/', UpdateOrders, name='order_update'),

]
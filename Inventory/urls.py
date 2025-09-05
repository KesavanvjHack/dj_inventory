from django.urls import include, path

from .views import *

urlpatterns = [

    # path('products/add/', ProductsAdd),
    # path('products/', AllProducts),
    # path('products/delete/<int:id>/', DeleteProducts, name='product_delete'),
    # path('products/update/<int:id>/', UpdateProducts, name='product_update'),
    
    
    path('products/add/', ProductsAddView.as_view()),
    path('products/', AllProductsView.as_view()),
    path('products/delete/<int:id>/', DeleteProductsView.as_view(), name='product_delete'),
    path('products/update/<int:id>/', UpdateProductsView.as_view(), name='product_update'),
]
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# --------------------- Customers ---------------------

@login_required(login_url='/')
def CustomersAdd(request):
    context = {'customer_form': Customer_Form()}
    if request.method == 'POST':
        customer_form = Customer_Form(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/orders/customers/')
    return render(request, 'customers_add.html', context)


@login_required(login_url='/')
def AllCustomers(request):
    context = {'all_customers': Customer.objects.all()}
    return render(request, 'customers.html', context)


@login_required(login_url='/')
def DeleteCustomers(request, id):
    selected_customer = Customer.objects.get(id=id)
    selected_customer.delete()
    return redirect('/orders/customers/')


@login_required(login_url='/')
def UpdateCustomers(request, id):
    selected_customer = Customer.objects.get(id=id)
    context = {'customer_form': Customer_Form(instance=selected_customer)}

    if request.method == 'POST':
        customer_form = Customer_Form(request.POST, request.FILES, instance=selected_customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/orders/customers/')

    return render(request, 'customers_add.html', context)


# --------------------- Orders --------------------------------------

@login_required(login_url='/')
def OrdersAdd(request):
    context = {'order_form': Order_Form()}

    if request.method == 'POST':
        selected_product = Product.objects.get(id=request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = (amount * selected_product.gst) / 100
        bill_amount = amount + gst_amount

        new_order = Order(
            customer_reference_id=request.POST['customer_reference'],
            product_reference_id=request.POST['product_reference'],
            order_number=request.POST['order_number'],
            order_date=request.POST['order_date'],
            quantity=request.POST['quantity'],
            amount=amount,
            gst_amount=gst_amount,
            bill_amount=bill_amount
        )
        new_order.save()
        return redirect('/orders/orders/')

    return render(request, 'orders_add.html', context)


@login_required(login_url='/')
def AllOrders(request):
    # Show all orders to everyone
    all_orders = Order.objects.all()
    context = {'all_orders': all_orders}
    return render(request, 'orders.html', context)


@login_required(login_url='/')
def DeleteOrders(request, id):
    selected_order = Order.objects.get(id=id)
    selected_order.delete()
    return redirect('/orders/orders/')


@login_required(login_url='/')
def UpdateOrders(request, id):
    order = Order.objects.get(id=id)
    context = {'order_form': Order_Form(instance=order)}

    if request.method == 'POST':
        selected_product = Product.objects.get(id=request.POST['product_reference'])
        amount = float(selected_product.price) * float(request.POST['quantity'])
        gst_amount = (amount * selected_product.gst) / 100
        bill_amount = amount + gst_amount

        Order.objects.filter(id=id).update(
            customer_reference_id=request.POST['customer_reference'],
            product_reference_id=request.POST['product_reference'],
            order_number=request.POST['order_number'],
            order_date=request.POST['order_date'],
            quantity=request.POST['quantity'],
            amount=amount,
            gst_amount=gst_amount,
            bill_amount=bill_amount
        )
        return redirect('/orders/orders/')

    return render(request, 'orders_add.html', context)

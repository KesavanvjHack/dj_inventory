from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *



def LoginPage(request):
    # If user is already logged in, redirect based on role
    if request.user.is_authenticated:
        if request.user.role == 0 or request.user.role == 1:      # type: ignore # Admin or Manager
            return redirect('/orders/customers/')
        else:
            return redirect('/orders/orders/')

    context = {"error": ""}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            # Role-based redirection
            if request.user.role == 0 or request.user.role == 1:      # type: ignore # Admin or Manager
                return redirect('/orders/customers/')
            else:                        # Customer
                return redirect('/orders/orders/')
        else:
            context["error"] = "* Invalid Username or Password"

    return render(request, 'login.html', context)


def LogoutUser(request):
    
    logout(request)
    
    return redirect('/')


def SignupPage(requset):
    
    context = {
        "error": "",
    
    }

    
    if requset.method == 'POST':
        
        check_user = User.objects.filter(username = requset.POST['username'])
        
        if len(check_user) > 0:
            
            context = {
                "error" : "* This Username is Already Exist?"
            }

            return render(requset, 'signup.html', context)
        
        else:
            
            new_user = User(username = requset.POST['username'], first_name = requset.POST['first_name'], last_name = requset.POST['last_name'], email = requset.POST['email'], age = requset.POST['age'], role = requset.POST['role'])
            
            new_user.set_password(requset.POST['password'])
            
            new_user.save()
    
            return redirect('/')
        
    return render(requset, 'signup.html', context)
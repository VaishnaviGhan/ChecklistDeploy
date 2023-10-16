from django.http import HttpResponse, JsonResponse, Http404
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from checkapp.forms import ChangePasswordForm
#from checkapp.genlib import Log
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterCustomerForm



def home(request,pk=None):
    if request.user.is_authenticated:
        print('Logged')
    else:
        print('not')
      
    variables = { 'page_title': 'Ashoka Buildcon Limited',
                  'username': request.user.get_full_name(), 
                  'isActive' : request.user.is_authenticated,
                  'isSuperUser' : request.user.is_superuser,
                  'app_title':'Document Inbox',
                  'isForm' : True,
                  'isHomePage' : True,
                  'customer_name' : 'Ashoka Buildcon Limited',
  
                }
    
    return render(request, 'checkapp/home.html', variables)
      
def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            variable = form.save(commit=False)
            variable.is_customer = True
            variable.save()
            messages.info(request,'<h2>Your Account has been Successfully Register...! Please Login</h2>')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong..! Please check form input ')
            return redirect('register-customer')
        
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request,'checkapp/register_customer.html',context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request,'Login Successful...!')
            return redirect('home')
        else:
            messages.warning(request,'Something went wrong..! please check input ')
            return redirect('login')
        
    else:
        return render(request,'checkapp/login.html')
    
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
       
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            msg = "Your password is changed"
            variables = { 'page_title': 'Ashoka Buildcon Limited',
                          'username': request.user.get_full_name(),
                          'isActive' : request.user.is_authenticated,
                          'isSuperUser' : request.user.is_superuser,
                          'isForm' : True,
                          'isHomePage' : True,
                          'customer_name' : 'Ashoka Buildcon Limited',
                          'successalert' : msg
                        }            
            return render(request, 'checkapp/home.html', variables)
        else:
            form = ChangePasswordForm(request.user)
            msg = 'Password do not match or incorrect passwords. Please try again'
            variables = { 'page_title': 'Ashoka Buildcon Limited',
                          'username': request.user.get_full_name(),
                          'isActive' : request.user.is_authenticated,
                          'isSuperUser' : request.user.is_superuser,
                          'isForm' : True,
                          'isHomePage' : True,
                          'customer_name' : 'Ashoka Buildcon Limited',
                          'successalert' : msg,
                          'form' : form,
                        }            
            return render(request, 'checkapp/change_password.html', variables)
    else:
        form = ChangePasswordForm(request.user)
        variables = { 'page_title': 'Ashoka Buildcon Limited',
                      'username': request.user.get_full_name(),
                      'isActive' : request.user.is_authenticated,
                      'isSuperUser' : request.user.is_superuser,
                      'app_title':'Document Inbox',
                      'isForm' : True,
                      'isHomePage' : True,
                      'customer_name' : 'Ashoka Buildcon Limited',
                      'form' : form,                     
                    }        
        return render(request, 'checkapp/change_password.html', variables)
    
def logout_user(request):
    logout(request)
    return redirect("/login") 


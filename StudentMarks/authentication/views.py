import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context_processors import csrf
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          form_instance = form.save(commit=False)
          form_instance.save()
          form_instance.refresh_from_db
          form_instance.userprofile.phone_number =form.cleaned_data['phone_number']
          form_instance.userprofile.address = form.cleaned_data['address']
          form_instance.save()

          messages.add_message(request, messages.SUCCESS, 'New User added Successfully.')
          return redirect('index')
        else:
            args = {'form':form}
            return render(request,'authentication/register-user.html',args)
    else:
        form = UserRegistrationForm()
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'authentication/register-user.html',args)

def sign_in(request):
  if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
          args = {'form':form}
          username = form.cleaned_data['username']
          password = form.cleaned_data['password']
          user = authenticate(username=username, password=password)
         
          if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'You have Logged in Successfully.')
            return redirect('index')
        
          else:
            messages.add_message(request, messages.ERROR, 'You have entered Wrong Username or Password.')
            return render(request,'authentication/login-user.html',args)
        else:
            args = {'form':form}
            return render(request,'authentication/login-user.html',args)
  else:
        form = UserLoginForm()
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'authentication/login-user.html',args)


def sign_out(request):
  logout(request)
  messages.add_message(request, messages.WARNING, 'You have Logged out Successfully.')
  return redirect('index')



def password_reset_complete(request):
    messages.add_message(request, messages.SUCCESS, 'You have reset your password Successfully.')
    return redirect('index')


from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from .models import Customer
from .forms import MyLoginForm,SignUpForm
from django.contrib.auth import authenticate,login,logout
from books.views import *
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            data = form.cleaned_data
            username = data["username"]
            password = data["password"]

            user = authenticate(request, username=username, password=password)
            
            print(user)
            
            # First check if user exists (authentication succeeded)
            if user is not None:
                # Then you can check if user is staff
                if user.is_staff:
                    # Staff user - do something special if needed
                    print("User authenticated as staff")
                # Log the user in (for both staff and regular users)
                login(request, user)
                print("User authenticated successfully")
                return redirect('home_view')
            else:
                # Authentication failed
                return render(request, "accounts/login.html", {
                    'form': form,
                    'error': 'Invalid username or password.'
                })
        else:
            print(form.errors)
            return render(request, "accounts/login.html", {
                'form': form,
                'error': 'Form is not valid. Please correct the errors.'
            })
    else:
        form = MyLoginForm()
        return render(request, "accounts/login.html", {'form': form})


def signup_view(request):
    if request.method == "post":
        form = SignUpForm(request.POST)
        if form.is_valid:
            user = form.save
            login(request,user)
            return redirect('home_view')
        else:
            print("form is invalidddddd")
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})    

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

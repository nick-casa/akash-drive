from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm


# Create your views here.

@login_required(login_url='login')
def index(response):
    return render(response, "main/index.html", {})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Profile successfully created for '+ user)
            return redirect('login')
        

    context = {'form':form}
    return render(request,'main/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Username OR Password is incorrect.')
    
    context = {}
    return render(request,'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
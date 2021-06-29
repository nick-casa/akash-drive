from main.models import Node
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, NodeForm


# Create your views here.

@login_required(login_url='login')
def index(request):
    form = NodeForm()

    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    context = {'form':form}
    return render(request, "main/index.html", context)

@login_required(login_url='login')
def trash(response):
    return render(response, "main/trash.html", {})

@login_required(login_url='login')
def shared(response):
    return render(response, "main/shared.html", {})


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

    
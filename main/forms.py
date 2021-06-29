from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from .models import Node, UserDetails

from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class NodeForm(ModelForm):
    class Meta:
        model = Node
        fields= '__all__'
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserDetails(models.Model):
    user_id = models.ForeignKey(User,null=True, on_delete=models.DO_NOTHING)
    wallet = models.CharField(max_length=100, null=True)


class Node(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    parent_folder_id = models.IntegerField(null=True)
    folder_id = models.BigIntegerField(null=True)
    is_folder = models.BigIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    location =  models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=50, null=True)
    last_modified = models.DateField(null=True)
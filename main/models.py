from django.contrib.auth.forms import UserCreationForm
from django.db import models

# Create your models here.

class UserDetails(models.Model):
    user_id = models.IntegerField()
    email = models.EmailField()
    wallet = models.CharField(max_length=100)


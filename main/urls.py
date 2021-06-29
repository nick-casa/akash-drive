from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("trash/", views.trash, name="trash"),
    path("shared/", views.shared, name="shared"),

]
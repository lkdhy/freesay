from django.urls import path

from . import views

urlpatterns = [
    path("hello", views.hello, name="helloTest"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("users/list", views.userslist, name="userlist"),
]
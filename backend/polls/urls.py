from django.urls import path

from . import views
from . import views_box

urlpatterns = [
    path("hello", views.hello, name="helloTest"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("users/list", views.userslist, name="userlist"),
    path("logout", views.logout, name="logout"),
    path("share", views_box.share, name="share"),
    path("box", views_box.box, name="box"),
    path("post", views_box.post, name="post"),
    path("gethostpost", views_box.gethostpost, name="gethostpost"),
    path("getpost", views_box.getpost, name="getpost"),
    path("answer", views_box.answer, name="answer"),
]
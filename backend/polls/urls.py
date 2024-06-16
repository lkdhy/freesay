from django.urls import path

from . import views
from . import views_box
from . import views_post
from . import view_tag
from . import views_thread
from . import views_public
from . import views_chat

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
    path("setsignature", views_post.setsignature, name="setsignature"),
    path("userinfo", views.userinfo, name="userinfo"),
    path("tags", view_tag.gettags, name="gettags"),
    path("thread", views_thread.appendthread, name="appendthread"),
    path("publicpost", views_public.publicpost, name="publicpost"),
    path("appendpublicpost", views_public.appendpublicpost, name="appendpublicpost"),
    # TODO
    path("appendchat", views_chat.appendchat, name="appendchat"),
    path("getchat", views_chat.getchat, name="getchat"),
]
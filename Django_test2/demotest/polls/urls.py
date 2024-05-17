from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLogin_view),
    path('index/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('toregister/register/', views.register_view),
]
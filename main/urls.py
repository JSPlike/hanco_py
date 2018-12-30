from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('join/', views.signup, name="join"),
    path('login/', views.signin, name="login"),
]

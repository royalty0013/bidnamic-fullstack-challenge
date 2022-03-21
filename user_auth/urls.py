from unicodedata import name
from django.urls import path
from .views import (
    user_login,
    register,
    user_logout,
)
   
app_name = "user_auth"
   
urlpatterns = [
    path("", user_login, name="login"),
    path("register/", register, name="register"),
    path("logout/", user_logout, name="logout"),
]
    

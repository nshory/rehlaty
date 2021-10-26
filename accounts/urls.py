

from django.urls import path , include
from . import views


app_name="accounts"

urlpatterns = [

    path('home',views.home),
    path('register',views.registerPage,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('myaccount', views.MyAccount, name='myaccount'),
    path('myadds', views.Myadds, name='myadds'),




]

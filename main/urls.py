from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("nfps/", views.nfps, name="NFPs"),
    path("contactus/", views.contactus, name="Contact Us"),
    path("success/", views.successView, name='success'),
    path("register/", views.registerPage, name = "register"),
    path("login/", views.loginPage, name = "login"),
    path("logout/", views.logoutUser, name="logout"),
    path("grant_application", views.grantApplication, name="Grant Application"),
    path('create_grant', views.createGrant, name="Create Grant"),
    path('grant_list', views.grant_list, name="grant_list"),
    path('my_grants', views.my_grants, name="my_grants"),
    path('my_applications', views.my_applications, name="my_applications"),
    path('nfp_donation', views.nfp_donation, name="nfp_donation"),
    path('indv_donation', views.indv_donation, name="indv_donation")
]
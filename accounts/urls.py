from . import views
from django.urls import path
from django.contrib import admin
from accounts.views import HomePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # landing page
    path('', views.HomePageView.as_view(), name='home'),












    
]
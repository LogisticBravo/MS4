"""
URLS to override allauth forms so as to
allow two froms on the login and signup page.
"""
from django.urls import path
from .import views

urlpatterns = [
    path('accounts/signup.html', views.CustomSignupView.as_view(), name='CustomSignupView'),
    path('accounts/login.html', views.CustomLoginView.as_view(), name='CustomLoginView'),
]

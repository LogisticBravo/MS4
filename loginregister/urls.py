"""
URLS to override allauth forms so as to
allow two froms on the login and signup page.
"""
from django.urls import path
from .import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='account_signup'),
    path('accounts/login/', views.login, name='CustomLoginView'),
]

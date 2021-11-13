""" Creates the URL's for the contact form """
from django.urls import path
from .import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]

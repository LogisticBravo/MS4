from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostView.as_view(), name='blog'),
]

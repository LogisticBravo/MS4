from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostView.as_view(), name='blog'),
    path('add/', views.CreatePostView.as_view(), name='add_post'),
]

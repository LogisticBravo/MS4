""" Creates the Url's for blogpost CRUD """
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.BlogPostView.as_view(), name='blog'),
    path('add/', views.CreatePostView.as_view(), name='add_post'),
    path('posts/<int:pk>', views.FullPostView.as_view(), name='post'),
    path('posts/edit/<int:pk>', login_required(views.EditPostView.as_view()),
         name='edit_post'),
    path('posts/<int:pk>/delete', login_required(
                                                 views.DeletePostView.as_view()
                                                 ), name='delete_post'),
]

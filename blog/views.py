from django.views.generic import ListView, CreateView, DetailView
from .models import BlogPosts

# Create your views here.


class BlogPostView(ListView):
    model = BlogPosts
    template_name = 'blog.html'


class CreatePostView(CreateView):
    model = BlogPosts
    template_name = "blog/add_post.html"
    fields = '__all__'

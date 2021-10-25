from django.views.generic import ListView
from . models import BlogPosts

# Create your views here.


class BlogPostView(ListView):
    model = BlogPosts
    template_name = 'blog.html'

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import BlogPosts
from django.urls import reverse_lazy

# Create your views here.


class BlogPostView(ListView):
    model = BlogPosts
    template_name = 'blog.html'
    ordering = ('-id')


class CreatePostView(CreateView):
    model = BlogPosts
    template_name = "blog/add_post.html"
    fields = '__all__'


class FullPostView(DetailView):
    model = BlogPosts
    template_name = 'post.html'


class EditPostView(UpdateView):
    model = BlogPosts
    template_name = 'edit_post.html'
    fields = ('title', 'body')


class DeletePostView(DeleteView):
    model = BlogPosts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')

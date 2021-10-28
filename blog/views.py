from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import BlogPosts

# Create your views here.


class BlogPostView(ListView):
    model = BlogPosts
    template_name = 'blog.html'
    ordering = ('-id')


class CreatePostView(SuccessMessageMixin, CreateView):
    model = BlogPosts
    template_name = "blog/add_post.html"
    fields = '__all__'
    success_message = "Post created successfully"


class FullPostView(DetailView):
    model = BlogPosts
    template_name = 'post.html'


class EditPostView(SuccessMessageMixin, UpdateView):
    model = BlogPosts
    template_name = 'edit_post.html'
    fields = ('title', 'body')
    success_message = 'Blog Post Edited'


class DeletePostView(DeleteView):
    model = BlogPosts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.error(self.request, 'Blog Post Deleted!')
        return response

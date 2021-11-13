""" View for CRUD elements of the blog posts """
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogPosts

# Create your views here.


class BlogPostView(ListView):
    """ A list view to display published blogposts """
    paginate_by = 8
    model = BlogPosts
    template_name = 'blog.html'
    ordering = ('-id')


class CreatePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """ A view to create a new blog post """
    model = BlogPosts
    template_name = "blog/add_post.html"
    fields = ['title', 'body']
    success_message = "Post created successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FullPostView(DetailView):
    """ A detail view for viewing an individual blog post """
    model = BlogPosts
    template_name = 'post.html'


class EditPostView(SuccessMessageMixin, UpdateView):
    """ An edit view to edit an existing blog posts content """
    model = BlogPosts
    template_name = 'edit_post.html'
    fields = ('title', 'body')
    success_message = 'Blog Post Edited'


class DeletePostView(DeleteView):
    """ A view to delete a blog post """
    model = BlogPosts
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.error(self.request, 'Blog Post Deleted!')
        return response

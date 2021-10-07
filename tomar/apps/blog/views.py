from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Post


# class HomePageView(generic.ListView):
#     """Show the home page of the website."""
#     template_name = "blog/index.html"
#     context_object_name = "posts"

#     def get_queryset(self):
#         return Post.objects.all()


def index(request):
    """Show the home page of the website."""
    featured_posts = Post.objects.all().order_by("-date_posted")[:4]
    all_posts = Post.objects.all()[4:]
    context = {
        "featured_posts": featured_posts,
        "all_posts": all_posts,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    """Show the detail of a single post."""

    model = Post
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    """Display post creation form and handle the process."""

    model = Post
    fields = ["category", "title", "content", "image"]
    template_name = "blog/post_create_form.html"

    def form_valid(self, form):
        # assign the current logged in user as author of the post
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Display post update form and handle the process."""

    model = Post
    fields = ["category", "title", "content", "image"]
    template_name = "blog/post_update_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # check that the person trying to update the post is owner of the post
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Display post deletion form and handle the process."""

    model = Post

    def get_success_url(self):
        # After deleting the post, redirect to user's profile page
        post_slug = self.kwargs["slug"]
        author = Post.objects.get(slug=post_slug).author
        return reverse_lazy("account:profile", args=(author.username,))

    def test_func(self):
        # check that the person trying to delete the post is owner of the post
        return self.get_object().author == self.request.user

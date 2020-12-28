from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    template_name = 'home.html'
    model = Post


class PostDetailView(generic.DetailView):
    template_name = 'post_details.html'
    model = Post

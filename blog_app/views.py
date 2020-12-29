from django.urls import reverse
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    template_name = 'home.html'
    model = Post


class PostDetailView(generic.DetailView):
    template_name = 'post_details.html'
    model = Post


class PostCreateView(generic.CreateView):
    template_name = 'post_create.html'
    model = Post
    fields = '__all__'
    # fields = ('title', 'content')

    def get_success_url(self):
        return reverse('post details', kwargs={'slug': self.object.slug})

from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import PostForm, EditPostForm
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
    form_class = PostForm

    # fields = ('title', 'content')

    def get_success_url(self):
        return reverse('post details',
                       kwargs={
                           'pk': self.object.pk,
                           'slug': self.object.slug,
                       })


class PostUpdateView(generic.UpdateView):
    template_name = 'post_update.html'
    model = Post
    form_class = EditPostForm

    def get_success_url(self):
        return reverse('post details',
                       kwargs={
                           'pk': self.object.pk,
                           'slug': self.object.slug,
                       })


class PostDeleteView(generic.DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('home')

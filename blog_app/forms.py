from django import forms

from common.bootstrap_form_mixin import BootstrapFormMixin
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for choice in choices:
    choices_list.append(choice)


class PostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    class Meta:
        model = Post
        fields = ('title', 'category', 'content', 'snippet', 'image')

        widgets = {'category': forms.Select(choices=choices_list,)}

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'author': forms.Select(attrs={'class': 'form-control'}),
        #     'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        #     'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        # }


class EditPostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    class Meta:
        model = Post
        fields = ('category', 'content', 'snippet')

        widgets = {'category': forms.Select(choices=choices_list,)}


        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        #     'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        #
        # }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control'})}

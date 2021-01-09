from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Profile
from .forms import SignUpForm, UserEditForm, PasswordsChangeForm, ProfileForm
from django.contrib.auth import forms


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    form_class = ProfileForm
    # fields = ('bio', 'profile_picture', 'fb_url', 'twitter_url', 'instagram')


class ProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    # def get_context_data(self, *args, **kwargs):
    #     user = get_object_or_404(Profile, id=self.kwargs['pk'])
    #     context = super().get_context_data(*args, **kwargs)
    #     context['user'] = user
    #     return context


def password_success(request):
    return render(request, 'registration/password_success.html')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordsChangeForm
    success_url = reverse_lazy('password success')


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = UserEditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


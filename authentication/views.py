from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import forms


class UserRegisterView(generic.CreateView):
    form_class = forms.UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


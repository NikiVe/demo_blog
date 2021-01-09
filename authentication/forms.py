from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model
from django import forms

from authentication.models import Profile
from common.bootstrap_form_mixin import BootstrapFormMixin

UserModel = get_user_model()


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.setup_form()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture', 'fb_url', 'twitter_url', 'instagram')


class SignUpForm(BootstrapFormMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #
    # class Meta:
    #     model = UserModel
    #     fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserEditForm(BootstrapFormMixin, UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class PasswordsChangeForm(BootstrapFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()

    # old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    # new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
    #     'class': 'form-control', 'type': 'password'
    # }))
    # new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
    #     'class': 'form-control', 'type': 'password'
    # }))
    #
    # class Meta:
    #     model = UserModel
    #     fields = ('old_password', 'new_password1', 'new_password2')

from django.urls import path
from django.contrib.auth import views as auth_view

from .views import UserRegisterView, UserEditView, PasswordsChangeView, password_success, ProfilePageView, \
    EditProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success/', password_success, name='password success'),
    path('<int:pk>/profile_page/', ProfilePageView.as_view(),  name='profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(),  name='edit profile page'),
    # path('password/', auth_view.PasswordChangeView.as_view(template_name='registration/change_password.html')),
]

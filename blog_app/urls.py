from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='post details'),
    path('create_post/', views.PostCreateView.as_view(), name='create post'),
]

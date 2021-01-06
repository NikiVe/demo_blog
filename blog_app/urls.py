from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='post details'),
    path('create_post/', views.PostCreateView.as_view(), name='create post'),
    path('update_post/<int:pk>/', views.PostUpdateView.as_view(), name='update post'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete post'),
    path('create_category/', views.CategoryCreateView.as_view(), name='create category'),
    path('category/<str:cats>/', views.category_view, name='category'),
    path('category_list/', views.category_list_view, name='category list'),
    path('like/<int:pk>/', views.like_view, name='like post'),
    path('comment/<int:pk>/<slug:slug>/', views.CommentView.as_view(), name='comment'),

]

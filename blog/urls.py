from django.urls import path
from .views import *


urlpatterns = [
    path('post/',add_post,name='add_post_url'),
    path('',home_view,name='home_url'),
    path('blog_details/<int:pk>/',blog_details,name='blog_details_url'),
    path('my_posts/',my_posts,name='my_posts_url'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    ]
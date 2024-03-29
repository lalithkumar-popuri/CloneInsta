from django.urls import path, re_path

from . import views

app_name = 'posts'

urlpatterns = [
    path("",views.PostList.as_view(),name = "all"),
    path("new/",views.CreatePost.as_view(),name = "create"),
    path("<username>/",views.UserPostList.as_view(),name = "profile"), 
]
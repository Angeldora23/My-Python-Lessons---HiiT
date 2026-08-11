from projectapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("my_profile/", views.my_profile, name="my_profile"),
    path("posts/", views.posts, name="posts"),
    path("post/<str:pk>/", views.post, name="post"),
    ]

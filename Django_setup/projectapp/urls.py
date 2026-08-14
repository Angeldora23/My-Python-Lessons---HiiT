from projectapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("my_profile/", views.my_profile, name="my_profile"),
    path("posts/", views.posts, name="posts"),
    path("posts/add/", views.add_post, name="add_post"),
    path("post/<str:pk>/", views.post, name="post"),

    path("user_form", views.display_form, name="user_form"),
    path("user_custom_create", views.custom_create_user, name="user_custom_create"),
    path("user_submit", views.submit_form, name="submit_form"),
]

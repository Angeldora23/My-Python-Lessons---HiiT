from projectapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("my_profile", views.my_profile, name="my_profile")
    
]

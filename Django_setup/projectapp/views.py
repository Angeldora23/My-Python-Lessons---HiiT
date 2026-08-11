from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from projectapp.models import Post


def home(request):
    return render(request, "index.html")


def about(request):
    about_message = "This is a Django project"

    best_players = ["Ororo", "Neymar", "Mbappe", "Dembele"]
    GOAT = "Messi"

    context = {
        "Pelumi": about_message,
        "programmer_name": "Dora",
        "programmer_age": 54,
        "programmer_class": "Python",
        "best_players": best_players,
        "GOAT": GOAT,
    }

    return render(request, "about.html", context)


def my_profile(request):
    profile = {
        "name": "Favour",
        "class": "Python",
        "age": 54,
    }
    return JsonResponse(profile)


def posts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts.html", context)

def post(request, pk):
    the_post = Post.objects.get(pk=pk)
    context = {"post": the_post}
    return render(request, "post.html", context)

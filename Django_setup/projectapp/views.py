from django.shortcuts import render, get_object_or_404, redirect
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
    context = {"Posts": posts}
    return render(request, "posts.html", context)

def post(request, pk):
    #the_post = Post.objects.get(pk=pk)
    the_post = get_object_or_404(Post, pk=pk)
    context = {"Post": the_post}
    return render(request, "post.html", context)


#this is defining the function and linking the user_login html to the url
def display_form(request):
    return render(request, "user_form.html")


def submit_form(request):
    if request.method =="POST":
        name = request.POST.get("name")
        dept = request.POST.get("department")

        values = {"name": name, "department": dept}
        return JsonResponse(values)

    return redirect("user_form")


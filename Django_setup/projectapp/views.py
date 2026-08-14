from django.core.checks import messages
from django.core.mail import message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from projectapp.forms import PostForm
from projectapp.models import Post
from django.contrib.auth.models import User

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

def add_post(request):
    form = PostForm()

    context = {"post_form": form}
    return render(request, "post_form.html", context)

#THIS IS DEFINING THE FUNCTION FOR CREATING USERS WITH THEIR LOGINS
# WE CREATED USING OUR OWN FORMS AND NOT PYTHON FORMS

def custom_create_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if not (username and email and password and confirm_password):
            messages.error(request, "All fields are required.")
            return redirect("user_custom_create")

        if User.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username taken.")
            return redirect("user_custom_create")

        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("user_custom_create")

        if password != confirm_password:
            messages.error(request, "Passwords must match.")
            return redirect("user_custom_create")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully.")
        return redirect("home")

    return render(request, "create_user.html")

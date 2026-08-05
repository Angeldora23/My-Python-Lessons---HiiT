from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home (request):
    return render(request, "index.html"),

def about(request):
    about_message = "This is a Django project"

    best_players = ["Ororo", "Neymar", "Mbappe", "Dembele"]
    GOAT = "Messi"

    context = {
        "Pelumi": about_message, 
        "programmer_name" : "Dora",
        "programmer_age": 54, 
        "programmer_class": "Python", 
        "best_players": best_players, 
        "GOAT": GOAT
    } 

    return render(request, "about.html", context)  


def my_profile(request):
    my_profile = { 
        "name": "Favour",
        "class":"Python",
        "age":54
          }
    return JsonResponse (my_profile)

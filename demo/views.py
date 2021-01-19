from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def Home(request):
    print("Home Page View")
    return HttpResponse("Home Page")
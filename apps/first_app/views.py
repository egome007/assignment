from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def time(request):
    context = {"time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def blogs(request):
    response = "Hello, I am blogs"
    return HttpResponse(response)

def new(request):
    response = "Hello, make a new form"
    return HttpResponse(response)

def create(request):
    response = "Hello, lets create"
    return HttpResponse(response)

def number(request):
    response = "Hello, lets create"
    return HttpResponse(response)


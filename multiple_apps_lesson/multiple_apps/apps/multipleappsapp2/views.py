from django.shortcuts import render, HttpResponse

def index(request):
    response = "Hello, this is app 2!"
    return HttpResponse(response)
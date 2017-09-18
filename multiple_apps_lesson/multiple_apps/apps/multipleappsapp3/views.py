from django.shortcuts import render, HttpResponse

def index(request):
    response = "Hello, this is app3!"
    return HttpResponse(response)
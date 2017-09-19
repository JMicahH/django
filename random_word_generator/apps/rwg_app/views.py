from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
        request.session['randomword'] = get_random_string(length=14)
    return render(request, 'rwg_app/index.html')

def generate(request):
    request.session['count'] += 1
    request.session['randomword'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    request.session['count'] = 1
    return redirect('/')

    
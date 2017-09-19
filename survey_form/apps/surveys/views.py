from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'surveys/index.html')

def processform(request):
    request.session['name'] = request.POST['name']
    request.session['dojoloc'] = request.POST['dojoloc']
    request.session['favlang'] = request.POST['favlang']
    request.session['comment'] = request.POST['comment']
    request.session['count'] += 1
    return redirect('/result')

def result(request):

    return render(request, 'surveys/result.html')

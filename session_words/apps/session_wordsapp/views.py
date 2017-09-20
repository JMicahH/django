from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


# Create your views here.
def index(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
        print "No Activity"
    return render(request, 'session_wordsapp/index.html')

def newword(request):
    # request.session['newword'] = request.POST['newword']
    # request.session['color'] = request.POST['color']
    # request.session['fontsize'] = request.POST.get('fontsize', "14px")
    # request.session['timestamp'] = strftime("%H:%M:%S %p, %B %d %Y", gmtime())
    print "BEFORE:::" 
    print request.session['activity']

    newword = {
        "newword"   : request.POST['newword'], 
        "color"     : request.POST['color'], 
        "fontsize"  : request.POST.get('fontsize', "14px"),
        "timestamp" : strftime("%H:%M:%S %p, %B %d %Y", gmtime())
    }

    request.session['activity'].append(newword)
    request.session.modified = True
    

    print "AFTER:::"
    print request.session['activity']
    return redirect('/')

def clearsession(request):
    for key in request.session.keys():
        del request.session[key]
    print request.session
    return redirect('/')



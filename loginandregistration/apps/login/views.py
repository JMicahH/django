from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib.messages import error
import bcrypt

from models import *

# Create your views here.
def index(request):
    indexload = "You've arrived at INDEX"
    print indexload

    return render(request, 'login/index.html')


def register(request):
    errors = Users.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)

        return redirect('index')

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    isnew = "yes"
    Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, isnew=isnew)

    active_user = Users.objects.get(email=email)
    request.session['active_user'] = active_user.id
    print 'SESSION USER'
    print request.session['active_user']

    return redirect(reverse('welcome_page'))


def login(request):
    errors = Users.objects.validate(request.POST)
    print "LOGIN ROUTE"

    if Users.objects.filter(email=request.POST['email']):
        active_user = Users.objects.get(email = request.POST['email'])
        print "EMAIL FOUND"
        request.session['active_user'] = active_user.id
        active_user.isnew = 'no'
        active_user.save()

        if bcrypt.checkpw(request.POST['password'].encode(), active_user.password.encode()):
            return redirect(reverse('welcome_page'))

        else:
            error(request, 'Your password was incorrect, please try again.')
            return redirect('index')
    
    else:
        print "EMAIL NOT FOUND"

        if len(errors): 
            for field, message in errors.iteritems():
                error(request, message, extra_tags=field)

            return redirect('index')
    


def welcome(request):
    print "WELCOME ROUTE"
    active_user_id = request.session['active_user']
    context = {
        'user' : Users.objects.get(id=active_user_id)
    }

    return render(request, 'login/welcome.html', context)


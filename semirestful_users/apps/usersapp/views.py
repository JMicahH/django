from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from models import *
# Create your views here.
def index(request):

    return render(request, 'usersapp/index.html', { 'users' : Users.objects.all() } )

def new(request):
    
    return render(request, 'usersapp/new.html')

def creation(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    Users.objects.create(first_name=first_name, last_name=last_name, email=email)
    return redirect('/')

def show(request, id):
    response = "Show User" + str(id)
    print response
    return render(request, 'usersapp/show.html', { 'chosen_user' : Users.objects.get(id=id) })


def edit(request, id):
    response = "Edit User" + str(id)
    print response
    return render(request, 'usersapp/edit.html', { 'chosen_user' : Users.objects.get(id=id) })


def update(request):        
    chosen_user = Users.objects.get(id= int(request.POST['id']))

    chosen_user.first_name = request.POST['first_name']
    chosen_user.last_name = request.POST['last_name']
    chosen_user.email = request.POST['email']
    chosen_user.save()

    status = "User with ID: " + request.POST['id'] + " UPDATED"
    print status
    return redirect(reverse('show_user', kwargs={'id' : chosen_user.id}))

def delete(request, id):
    chosen_user = Users.objects.get(id=id)
    chosen_user.delete()
    print "DELETED User " + id 
    return redirect('/')

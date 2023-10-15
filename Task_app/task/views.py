from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task
from .forms import TaskForm


def landing_page(request):
    return render(request, 'landing.html')


#User login
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are successfully logged in.."))
            return redirect('home/')
        else:
            messages.success(request, ("There was an error logging in. Try again..."))
            return redirect('login')    
    else:        
        return render(request, 'login.html')


#User logout
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out!.."))
    return redirect('/')


#User Register


#Create
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        item = Task.objects.all()
        if form.is_valid():
            form.save()
            return redirect('task_view')         
   
    item = Task.objects.all()
    return render(request, 'home.html', {'item': item})



#Retrieve
def task_view(request):
    form = TaskForm(request.POST)
    item = Task.objects.all()
    if form.is_valid():
        form.save()
        return render(request, 'task_view.html', {'item': item})
    return render(request, 'task_view.html', {'item': item})


#Update
def update(request, id):
    pass


#Delete
def delete(request, id):
    item = Task.objects.get(id=id)    
    item.delete()
    return redirect('task_view')


from django.shortcuts import render
from .models import Task
from .forms import TaskForm
# Create your views here.

def home(request):
        
    if request.method == 'POST':
        form = TaskForm()
        item = Task.objects.all()
        if form.is_valid():
            form.save()            
            return render(request, 'home.html', {'item': item})

    
    item = Task.objects.all()
    return render(request, 'home.html', {'item': item})
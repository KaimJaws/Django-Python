from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/home.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        title_task = request.POST.get('title')
        if title_task:
            Task.objects.create(title=title_task)
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')
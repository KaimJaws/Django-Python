from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from .models import Task

def tasks_list(request: HttpRequest) -> HttpResponse:
    pending_tasks: QuerySet[Task] = Task.objects.filter(completed=False)
    completed_tasks: QuerySet[Task] = Task.objects.filter(completed=True)

    context = {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks
    }

    return render(request, 'myapp/home.html', context)

def create_task(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title_task: str = request.POST.get('title')
        description_task: str = request.POST.get('description', '')
        if title_task:
            Task.objects.create(title=title_task, description=description_task)
    return redirect('home')

def delete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task: Task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def complete_task(request: HttpRequest, task_id: int) -> HttpResponse:
    task: Task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')
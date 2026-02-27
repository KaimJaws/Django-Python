from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.tasks_list,
        name='home'
    ),
    path(
        'edit/<int:task_id>/',
        views.tasks_list,
        name='edit_view'
    ),
    path(
        'tasks/create/',
        views.create_task,
        name='create_task'
    ),
    path(
        'tasks/update/<int:task_id>/',
        views.update_task,
        name='update_task'
    ),
    path(
        'tasks/delete/<int:task_id>/',
        views.delete_task,
        name='delete_task'
    ),
    path(
        'tasks/complete/<int:task_id>/',
        views.complete_task,
        name='complete_task'
    ),
    path(
        'tasks/uncomplete/<int:task_id>/',
        views.uncomplete_task,
        name='uncomplete_task'
    ),
]
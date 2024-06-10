from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import CreateView

from main.models import Todo, Task


def home(request):
    todo_list = Task.objects.none()
    task_list = Task.objects.none()

    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user)
        task_list = Task.objects.filter(user=request.user)

    todo_paginator = Paginator(todo_list, 5)
    task_paginator = Paginator(task_list, 5)

    todo_page_number = request.GET.get('todo_page', 1)
    task_page_number = request.GET.get('task_page', 1)

    todos = todo_paginator.page(todo_page_number)
    tasks = task_paginator.page(task_page_number)

    context = {
        'todos': todos,
        'tasks': tasks,
    }

    return render(request, 'main/home.html', context)


class TodoCreate(CreateView):
    model = Todo
    fields = ['category', 'title', 'done', 'priority', 'start_date', 'end_date', 'interval', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

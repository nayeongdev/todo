from django.shortcuts import render
from django.views.generic import CreateView

from main.models import Todo, Task


def home(request):
    todo_list = Task.objects.none()
    task_list = Task.objects.none()

    if request.user.is_authenticated:
        todo_list = Todo.objects.filter(user=request.user)
        task_list = Task.objects.filter(user=request.user)

    context = {
        'todo_list': todo_list,
        'task_list': task_list,
    }

    return render(request, 'main/home.html', context)


class TodoCreate(CreateView):
    model = Todo
    fields = ['category', 'title', 'done', 'priority', 'start_date', 'end_date', 'interval', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

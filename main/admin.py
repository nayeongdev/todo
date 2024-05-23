from django.contrib import admin

from main.models import Todo, Category, Task

admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Task)

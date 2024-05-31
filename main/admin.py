from django.contrib import admin

from main.models import Todo, Category, Task, Notification

admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Task)
admin.site.register(Notification)

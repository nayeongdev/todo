from django.contrib import admin

from main.models import Todo, Category, Task, Notification

admin.site.register(Notification)
admin.site.register(Category)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'interval')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

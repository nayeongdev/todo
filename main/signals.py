from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Todo
from .tasks import create_task


@receiver(post_save, sender=Todo)
def schedule_task_creation(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: create_task.delay(instance.id))

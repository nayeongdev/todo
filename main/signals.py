from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Todo, Task, Notification
from .tasks import create_task


@receiver(post_save, sender=Todo)
def schedule_task_creation(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: create_task.delay(instance.id))

@receiver(post_save, sender=Task)
def notify_task_creation(sender, instance, created, **kwargs):
    if created:
        notification = Notification.objects.create(
            user=instance.user,
            message=f"New task created: {instance.title}"
        )

        event_data = {
            'type': 'send_message',
            'message': notification.message
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)('notification', event_data)

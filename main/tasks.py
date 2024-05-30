import logging

from celery import shared_task
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ObjectDoesNotExist
from .models import Todo, Task

logger = logging.getLogger(__name__)


@shared_task
def create_task(todo_id):
    logger.info(f'Starting create_task for todo_id: {todo_id}')

    try:
        todo = Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        logger.warning(f"Todo with id {todo_id} does not exist.")
        return

    start_date = todo.start_date if todo.start_date else datetime.now().date()
    end_date = todo.end_date if todo.end_date else start_date + timedelta(days=365)
    interval = todo.interval

    current_date = start_date

    while current_date <= end_date:
        try:
            existing_task = Task.objects.get(todo=todo, created_at=current_date)
        except ObjectDoesNotExist:
            Task.objects.create(
                user=todo.user,
                todo=todo,
                title=todo.title,
                priority=todo.priority,
                created_at=current_date
            )
            logger.info(f"Created task for Todo {todo_id} on {current_date}")

            if interval == 'daily':
                current_date += timedelta(days=1)
            elif interval == 'weekly':
                current_date += timedelta(weeks=1)
            elif interval == 'monthly':
                current_date += relativedelta(months=1)
            else:
                break

    logger.info(f"Finished creating tasks for Todo {todo_id}")

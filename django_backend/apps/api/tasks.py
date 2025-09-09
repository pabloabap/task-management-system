from celery import shared_task
from django.core.mail import send_mail
from ..users.models import User
from ..tasks.models import Task

@shared_task
def send_task_notification(task_pk, notification_type):
	users = User.objects.all()
	if task_pk:
		task = Task.objects.get(pk=task_pk)
		send_mail(
			f'[{notification_type.upper()}] - {task.title}',
			str(task),
			"no-reply@task-management-system.com",
			[user.email for user in users],
			fail_silently=False
		)
	else:
		send_mail(
			f'[{notification_type.upper()}]',
			"One task was deleted",
			"no-reply@task-management-system.com",
			[user.email for user in users],
			fail_silently=False
		)
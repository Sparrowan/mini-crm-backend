from celery import shared_task
from datetime import datetime
from django.core.mail import send_mail
from .models import Reminder

@shared_task
def process_pending_reminders():
    now = datetime.now()
    pending_reminders = Reminder.objects.filter(status='pending', schedule_at__lte=now)

    for reminder in pending_reminders:
        reminder.status = 'processed'
        reminder.save()

    return f"Processed {len(pending_reminders)} reminders."
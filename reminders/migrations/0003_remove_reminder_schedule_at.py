# Generated by Django 5.1.4 on 2025-01-05 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_reminder_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='schedule_at',
        ),
    ]
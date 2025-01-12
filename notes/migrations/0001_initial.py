# Generated by Django 5.1.4 on 2025-01-04 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='leads.lead')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]

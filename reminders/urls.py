from .views import (
    ReminderCreateView, ReminderListView, 
    ReminderRetrieveView, ReminderUpdateView, 
    ReminderDestroyView
)
from django.urls import path

app_name = 'reminders'

urlpatterns = [
    path('list/', ReminderListView.as_view(), name='reminder-list'),
    path('create/', ReminderCreateView.as_view(), name='reminder-create'),
    path('<int:pk>/', ReminderRetrieveView.as_view(), name='reminder-retrieve'),
    path('<int:pk>/update/', ReminderUpdateView.as_view(), name='reminder-update'),
    path('<int:pk>/delete/', ReminderDestroyView.as_view(), name='reminder-delete'),
]
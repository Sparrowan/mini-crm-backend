from .views import (
    LeadCreateView, LeadListView, 
    LeadRetrieveView, LeadUpdateView, 
    LeadDestroyView
)
from django.urls import path

app_name = 'leads'

urlpatterns = [
    path('list/', LeadListView.as_view(), name='lead-list'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadRetrieveView.as_view(), name='lead-retrieve'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDestroyView.as_view(), name='lead-delete'),
]
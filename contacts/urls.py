from .views import (
    ContactCreateView, ContactListView, 
    ContactRetrieveView, ContactUpdateView, 
    ContactDestroyView
)
from django.urls import path

app_name = 'contacts'

urlpatterns = [
    path('list/', ContactListView.as_view(), name='contact-list'),
    path('create/', ContactCreateView.as_view(), name='contact-create'),
    path('<int:pk>/', ContactRetrieveView.as_view(), name='contact-retrieve'),
    path('<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('<int:pk>/delete/', ContactDestroyView.as_view(), name='contact-delete'),
]
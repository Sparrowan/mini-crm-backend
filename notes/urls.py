from .views import (
    NoteCreateView, NoteListView, 
    NoteRetrieveView, NoteUpdateView, 
    NoteDestroyView
)
from django.urls import path

app_name = 'notes'

urlpatterns = [
    path('list/', NoteListView.as_view(), name='note-list'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:pk>/', NoteRetrieveView.as_view(), name='note-retrieve'),
    path('<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('<int:pk>/delete/', NoteDestroyView.as_view(), name='note-delete'),
]
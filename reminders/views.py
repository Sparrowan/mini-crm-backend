from django.shortcuts import render
from .serializers import ReminderSerializer
from .models import Reminder
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from leads.models import Lead


class ReminderCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()
    
    def perform_create(self, serializer, *args, **kwargs):
        lead_id = self.request.data.get('lead_id', None)
        if lead_id is not None:
            try:
                lead = Lead.objects.get(id=lead_id)
                serializer.save(lead=lead)
            except Lead.DoesNotExist:
                return Response({"message": "Invalid lead_id"}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "lead_id is required"}, status=HTTP_400_BAD_REQUEST)


class ReminderListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()


class ReminderRetrieveView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()


class ReminderUpdateView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ReminderSerializer
    queryset = Reminder.objects.all()

    def perform_update(self, serializer):
        lead_id = self.request.data.get('lead_id', None)
        if lead_id is not None:
            try:
                lead = Lead.objects.get(id=lead_id)
                serializer.save(lead=lead)
            except Lead.DoesNotExist:
                raise ValueError("Invalid lead_id")
        else:
            serializer.save()


class ReminderDestroyView(DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Reminder.objects.all()

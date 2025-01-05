from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny
from leads.models import Lead


class ContactCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    
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


class ContactListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer

    def get_queryset(self):
        lead_id = self.request.query_params.get('lead_id', None)

        if lead_id:
            return Contact.objects.filter(lead_id=lead_id)
        
        return Contact.objects.all()



class ContactRetrieveView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactUpdateView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

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


class ContactDestroyView(DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Contact.objects.all()

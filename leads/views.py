from django.shortcuts import render
from .serializers import LeadSerializer
from .models import Lead
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import AllowAny

class LeadCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class LeadListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class LeadRetrieveView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class LeadUpdateView(UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

class LeadDestroyView(DestroyAPIView):
    permission_classes = (AllowAny,)
    queryset = Lead.objects.all()

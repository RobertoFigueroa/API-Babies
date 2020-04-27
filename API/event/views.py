from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from event.models import Event
from event.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
  queryset =  Event.objects.all()
  serializer_class = EventSerializer

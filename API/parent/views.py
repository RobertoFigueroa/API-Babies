from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from parent.models import Parent
from parent.serializers import ParentSerializer

class ParentViewSet(viewsets.ModelViewSet):
  queryset =  Parent.objects.all()
  serializer_class = ParentSerializer


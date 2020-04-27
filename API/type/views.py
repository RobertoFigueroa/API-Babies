from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from type.models import Type
from type.serializers import TypeSerializer

class TypeViewSet(viewsets.ModelViewSet):
  queryset =  Type.objects.all()
  serializer_class = TypeSerializer

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from baby.models import Baby
from baby.serializers import BabySerializer

class BabyViewSet(viewsets.ModelViewSet):
  queryset =  Baby.objects.all()
  serializer_class = BabySerializer

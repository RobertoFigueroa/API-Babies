from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from event.models import Event
from event.serializers import EventSerializer
from baby.serializers import BabySerializer
from rest_framework.response import Response
from permissions.services import APIPermissionClassFactory
from guardian.shortcuts import assign_perm



class EventViewSet(viewsets.ModelViewSet):
  queryset =  Event.objects.all()
  serializer_class = EventSerializer
  permission_classes = (
        APIPermissionClassFactory(
            name='EventPermissions',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                    
                },
                'instance': {
                    'retrieve': 'event.view_event',
                    'destroy': 'event.delete_event',
                    'update': True,
                    'partial_update':False,
                    # 'update_permissions': 'users.add_permissions'
                    # 'archive_all_students': phase_user_belongs_to_school,
                    # 'add_clients': True,
                }
            }
        ),
    )

  def perform_create(self, serializer):
    event = serializer.save()
    user = self.request.user
    assign_perm('event.view_event', user, event)
    assign_perm('event.delete_event', user, event)
    return Response(serializer.data)
from rest_framework import serializers

from baby.models import Baby
from type.models import Type
from event.models import Event

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = (
      'id',
      'note',
      'date',
      'event_type',
      'baby',
      'type'
    )

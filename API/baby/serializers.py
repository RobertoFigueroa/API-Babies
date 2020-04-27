from rest_framework import serializers

from baby.models import Baby
from parent.serializers import ParentSerializer

class BabySerializer(serializers.ModelSerializer):
  class Meta:
    model = Baby
    fields = (
      'id',
      'name',
      'last_name',
      'parent'
    )
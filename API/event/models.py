from django.db import models

class Event(models.Model):
  date = models.DateField()
  note = models.CharField(max_length=300)
  event_type = models.ForeignKey(
    'type.Type',
    on_delete=models.CASCADE,
    null = True,
    blank = True
  )
  baby = models.ForeignKey(
    'baby.Baby',
    on_delete=models.CASCADE,
    null = True,
    blank = True
  )

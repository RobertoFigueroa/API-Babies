from django.db import models

class Type(models.Model):
  name = models.CharField(max_length=60)

  def __str__(self):
    return self.name
  
  
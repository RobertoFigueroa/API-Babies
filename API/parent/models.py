from django.db import models


class Parent(models.Model):
  name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)


  def __str__(self):
    return 'Parent: {}'.format(self.name)
from django.db import models
from django.contrib.auth.models import User

class Baby(models.Model):
  name = models.CharField(max_length=30, null=False)
  last_name = models.CharField(max_length=30, null=False)
  # parent = models.ForeignKey(
  #   'parent.Parent',
  #   on_delete = models.CASCADE,
  #   null = True,
  #   blank = True
  # )

  parent = models.ForeignKey(User,
    on_delete=models.CASCADE,
    null=True
  )

  def __str__(self):
    return 'Baby: {}, {}'.format(self.name, self.last_name)

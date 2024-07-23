from django.db import models
from django.utils import timezone


class Problem(models.Model):
  name = models.CharField(max_length=60)
  regnum = models.CharField(max_length=60)
  phno = models.PositiveIntegerField()
  bhawan = models.CharField(max_length=20, null=True)
  rmnum = models.PositiveIntegerField()
  problem = models.TextField()
  created_date = models.DateField(default=timezone.now)
  created_time = models.TimeField(default=timezone.now)

  def __str__(self):
      return f"{self.name}-{self.rmnum}"

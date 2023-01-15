from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    completed = models.BooleanField(default=False)
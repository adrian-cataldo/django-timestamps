from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

""" extend from TimestampsModel instead of models.Model to support created_at and updated_at """

class TimestampsModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True




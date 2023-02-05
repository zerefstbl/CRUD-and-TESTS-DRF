from rest_framework import serializers

from .models import Task

from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['id', 'title']
    
  def save(self, **kw):
    task = super().save(**kw)
    task.updated_at = timezone.now()
    task.save()
    
    return task
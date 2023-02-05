from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=100, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)  
  
  def __str__(self):
    return self.title
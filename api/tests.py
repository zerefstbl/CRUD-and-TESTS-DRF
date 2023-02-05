import json
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from rest_framework.test import APIClient

from .models import Task

class Teste(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.valid_data = {
      'title': 'O retorno'
    }
    self.invalid_data = {
      'title': ''
    }
    
    self.update_task = {
      'title': 'Edited title'
    }
    
    self.task = Task.objects.create(title='O retorno')

    self.api = f'/api/tasks/{self.task.id}/'
    
   # Creating a task with a valid data 
  def teste_create_valid_task(self):
    response = self.client.post('/api/tasks/', json.dumps(self.valid_data), content_type='application/json')
        
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
  # Creating a task with a valid data 
  def teste_create_invalid_data(self):
    response = self.client.post('/api/tasks/', json.dumps(self.invalid_data), content_type='application/json')
    
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  
  # Sould return a correct task
  def teste_retrieve_correct_data(self):
    response = self.client.get(self.api)
    self.assertEqual(response.data, {'id': self.task.id, 'title': 'O retorno'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  
  # Should update a task and return 200 status code
  def teste_udpate_task(self):
    response = self.client.put(self.api, json.dumps(self.update_task), content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data, {'id': self.task.id, 'title': 'Edited title'})
  
  # Should not update a task with invalid data
  def teste_invalid_update_task(self):
    response = self.client.put(self.api, json.dumps(self.invalid_data), content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  
  # Should delete a task and return nothing
  teste_delete_task = lambda self: self.assertEqual(self.client.delete(self.api).status_code, status.HTTP_204_NO_CONTENT)
  
  # Should not delete a task that does not exist
  teste_invalid_delete_tasl = lambda self: self.assertEqual(self.client.delete(f'/api/tasks/5/').status_code, status.HTTP_404_NOT_FOUND)
  
  # Sould returns a correct number of all tasks
  teste_get_all__tasks = lambda self: self.assertEqual(len(Task.objects.all()), 1)
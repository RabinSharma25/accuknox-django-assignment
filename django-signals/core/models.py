
# these are migration scripts you must run them first to create the required tables
'''
python3 manage.py makemigrations core
python3 manage.py migrate

'''
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

class Car(models.Model):
    name = models.CharField(max_length=100)

class BookLog(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

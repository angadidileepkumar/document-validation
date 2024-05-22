# models.py
from django.db import models

class YourModel(models.Model):
    # Define your model fields here
    candidate_ID = models.CharField(max_length=100)
    candidate_name = models.CharField(max_length=50)
    pho = models.BigIntegerField()
    # ... add more fields as needed

    def __str__(self):
        return self.candidate_ID
   
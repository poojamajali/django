from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Job(models.Model):
    Job_role = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    location = models.TextField()
    salary = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
   

    def __str__(self):
        return self.Job_role

    def get_absolute_url(self):
        return reverse('job-home')


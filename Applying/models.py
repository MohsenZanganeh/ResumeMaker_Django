from django.db import models
from Candidate.models import Candidate
from Employee.models import Job
# Create your models here.
class Applied_Job(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    def __str__(self):
        return self.job
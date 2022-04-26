from django.db import models
from django.conf import settings
# Create your models here.
class Employee(models.Model):
    company_name = models.CharField(max_length=255)
    Employee_members = models.IntegerField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
    
    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name
        
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Employee = models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.title
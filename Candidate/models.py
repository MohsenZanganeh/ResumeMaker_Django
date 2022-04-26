from django.db import models
from django.conf import settings

# Create your models here.
class Candidate(models.Model):
    MALE = 'M'
    FEMAIL = 'F'
    GENDER_CHOICES = [
        (MALE,'Male'),
        (FEMAIL,'Femail')
    ] 
    national_id = models.IntegerField()
    detail = models.TextField()
    career = models.CharField(max_length=50)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name
        
    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    Candidate = models.ForeignKey(Candidate,on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.title
BESICE = 'B'
INTERMEDIATE = 'I'
PROFESSIONAL = 'P'
LEVEL_CHOICES = [
    (BESICE,'Basic'),
    (INTERMEDIATE,'Intermediate'),
    (PROFESSIONAL,'Professional'),
]

class Skill(models.Model):
    skill = models.CharField(max_length=255)
    level = models.CharField(max_length=1,choices=LEVEL_CHOICES)
    Candidate = models.ForeignKey(Candidate,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.skill
class Language(models.Model):
    language = models.CharField(max_length=50)
    level    = models.CharField(max_length=1,choices=LEVEL_CHOICES)
    Candidate = models.ForeignKey(Candidate,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.language
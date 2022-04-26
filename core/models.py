from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    EMPLOYEE = 'E'
    CANDIDATE = 'C'
    USER_TYPE = [
        (EMPLOYEE,'Employee'),
        (CANDIDATE,'Candidate')
    ]
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=1,choices=USER_TYPE,default='E')
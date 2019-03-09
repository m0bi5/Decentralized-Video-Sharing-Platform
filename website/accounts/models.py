from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Balance(models.Model):
    user_name=models.CharField(default='',max_length=100)
    amount=models.IntegerField(default=1000)
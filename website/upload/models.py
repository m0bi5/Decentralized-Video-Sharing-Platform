from django.db import models
import os


class UploadedFiles(models.Model):
	title=models.CharField(max_length=1000,default='')
	user=models.CharField(max_length=1000,default='')
	views=models.IntegerField(default=0)
	description=models.CharField(max_length=1000,default='')
	tags=models.CharField(max_length=1000,default='')
	fileHash=models.CharField(max_length=1000,default='')
	file=models.FileField()

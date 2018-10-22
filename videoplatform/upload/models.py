from django.db import models

class UploadedFiles(models.Model):
	fileName=models.CharField(max_length=1000,default='')
	fileHash=models.CharField(max_length=1000,default='')
	file=models.FileField()
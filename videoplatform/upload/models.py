from django.db import models

class UploadedFiles(models.Model):
	file=models.FileField()
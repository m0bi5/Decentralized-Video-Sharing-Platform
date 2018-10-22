from django.shortcuts import render
from . models import UploadedFiles
def upload(request):
	context={}
	if request.POST:
		obj=UploadedFiles(file=request.FILES['file'])
		obj.save()
	return render(request,'upload/upload.html',context)
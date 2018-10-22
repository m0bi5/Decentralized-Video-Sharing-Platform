from django.shortcuts import render
from . models import UploadedFiles
from . import ipfs
import os


def upload(request):
	context={'fileName':'','fileHash':'','url':''}
	if request.POST:
		obj=UploadedFiles(file=request.FILES['file'],fileName=request.FILES['file'].name)
		obj.save()
		base_path=os.getcwd()
		context['fileName']='media\\'+obj.fileName
		fileHash=ipfs.fileUpload(context['fileName'])
		context['fileHash']=obj.fileHash
		context['url']='http://www.ipfs.io/ipfs/'+context['fileHash']
		


	return render(request,'upload/upload.html',context)
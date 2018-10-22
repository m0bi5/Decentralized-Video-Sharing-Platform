from django.shortcuts import render
from . models import UploadedFiles
from . import ipfs
import time
import os

def upload(request):
	context={'fileName':'','fileHash':'','url':''}

	if request.POST:
		base_path=os.getcwd()
		obj=UploadedFiles(file=request.FILES['file'],fileName=base_path+'/media/'+request.FILES['file'].name)
		obj.fileHash=ipfs.fileUpload(request.FILES['file'].name)
		obj.save()
		context['fileName']=obj.fileName
		context['fileHash']=obj.fileHash
		context['url']='http://www.ipfs.io/ipfs/'+context['fileHash']
		
	return render(request,'upload/upload.html',context)
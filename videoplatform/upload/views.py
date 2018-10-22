from django.shortcuts import render
from . models import UploadedFiles
from . import ipfs
import time
import os
import platform

def upload(request):
	context={'fileName':'','fileHash':'','url':''}

	if request.POST:
		base_path=os.getcwd()
		#Take care of Windows file naming system
		if platform.system()=="Windows": 
			path=os.path.join(base_path,'media',request.FILES['file'].name)
		else:
			path=base_path+'/media/'+request.FILES['file'].name
		obj=UploadedFiles(file=request.FILES['file'],fileName=path)
		obj.save()
		obj.fileHash=ipfs.fileUpload(path)
		obj.save()
		context['fileName']=obj.fileName
		context['fileHash']=obj.fileHash
		context['url']='http://ipfs.io/ipfs/'+context['fileHash']
		
	return render(request,'upload/upload.html',context)
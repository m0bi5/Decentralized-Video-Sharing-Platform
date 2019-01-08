from django.shortcuts import render,redirect
from . models import UploadedFiles
from . import ipfs
from .forms import UploadForm
import time,shutil,os,platform
from django.core.files.storage import FileSystemStorage

def upload(request):
	if request.user.is_authenticated():
		context={'fileName':'','fileHash':'','url':'','form':UploadForm()}
		a=0
		if request.POST:
			base_path=os.getcwd()
			myfile = request.FILES['file']
			path=str(os.path.join(base_path))
			try:
				os.mkdir('media')
			except:
				print('Folder exists')
			obj=UploadedFiles(user=request.user.username,file=request.FILES['file'],title=request.POST['title'],description=request.POST['description'],tags=request.POST['tags'])
			path=str(os.path.join(path,obj.file.name))
			obj.save()
			obj.fileHash=ipfs.fileUpload(path)
			os.system('rm "'+path+'"')
			obj.save()
			context['fileHash']=obj.fileHash
			context['url']='http://ipfs.io/ipfs/'+context['fileHash']
			
		return render(request,'upload.html',context)
	else:
		return redirect('login')

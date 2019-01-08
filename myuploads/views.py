from django.shortcuts import render,redirect
from upload.models import UploadedFiles


# Create your views here.

def uploads(request):
	if request.user.is_authenticated():
		videos=UploadedFiles.objects.filter(user=request.user.username)
		context={'videos':videos}
		for i in videos:
			i.tags=i.tags.split(',')
		return render(request,'myuploads.html',context)
	else:
		return redirect('login')


def delete_video(request):
	if request.user.is_authenticated():
		UploadedFiles.objects.filter(fileHash=request.GET['video']).delete()
		videos=UploadedFiles.objects.filter(user=request.user.username)
		context={'videos':videos}
		return render(request,'myuploads.html',context)
	else:
		return redirect('login')
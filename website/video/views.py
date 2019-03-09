from django.shortcuts import render
from upload.models import UploadedFiles

# Create your views here.
def view_video(request,fileHash):
    video=UploadedFiles.objects.filter(fileHash=fileHash)

    if len(video)>0:
        video=video[0]
        video.views+=1
        video.save()
        context={'donateable':True,'video':video,'e404':False}
        if request.user.username==video.user:
            context['donateable']=False
        video.tags=video.tags.split(',')
    else:
        context['e404']=True
    
    return render(request,'view_video.html',context)
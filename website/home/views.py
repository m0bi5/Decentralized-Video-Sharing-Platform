
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from upload.models import UploadedFiles
from django.contrib import messages
from accounts.models import Balance
import json,requests

nodes=["http://localhost:5100/transactions/new","http://localhost:5000/transactions/new"]
def home(request):
    videos=UploadedFiles.objects.order_by('-views')[:20]
    return render(request,'home.html',{'videos':videos})

def search(request):
    context={}
    videos=UploadedFiles.objects.filter(tags__contains=request.POST['query']).order_by('-views')
    context={'videos':videos}
    for i in videos:
        i.tags=i.tags.split(',')
    return render(request,'search.html',context)

def getBalance(request):
    amount=Balance.objects.filter(user_name=request.user.username)[0].amount
    some_data_to_dump = {
    'amount': amount
    }

    data = json.dumps(some_data_to_dump)
    return HttpResponse(data, content_type='application/json')

def donate(request,hash):        
    obj=Balance.objects.filter(user_name=request.user.username)[0]
    obj_to=Balance.objects.filter(user_name=request.POST['donate_to'])[0]
    if obj.amount>=int(request.POST['amount'] and int(request.POST['amount'])>0):
        for node in nodes:
            data={"sender":request.user.username,"recipient":request.POST['donate_to'],"amount":int(request.POST['amount'])}
            r = requests.post(url = node, headers={"content-type":"application/json"}, json = data) 
        obj.amount-=int(request.POST['amount'])
        obj.save()
        obj_to.amount+=int(request.POST['amount'])
        obj_to.save()
        messages.success(request,'Balance deducted, transaction broadcasted to Blockchain')
        return redirect('view_video',hash)
    else:
        messages.danger(request,'Insufficient balance')
        return redirect('view_video',hash)
    

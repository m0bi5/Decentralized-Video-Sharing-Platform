
from django.shortcuts import get_object_or_404, redirect, render


def home(request):
    return render(request,'home.html',{})
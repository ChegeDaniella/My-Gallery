from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def firstImages(request):
    return render(request,'all-images/first-images.html')    

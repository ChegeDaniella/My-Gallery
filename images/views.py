from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def index(request):
    return render(request,'index.html')

def firstImages(request):
    SeeImage = Image.image_name
    return render(request,'all-images/first-images.html', {"name" : SeeImage} )    

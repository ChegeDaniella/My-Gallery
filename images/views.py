from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

def index(request):
    return render(request,'index.html')

def anime(request):
    SeeImage = Image.objects.all()
    args={"SeeImage" : SeeImage}
    return render(request,'all-images/first-images.html',args) 

def malawi(request):
    image = Image.objects.filter(image_location_id="1")
    context ={
        "post":image
    }
    return render(request,'all-images/first-images.html',context)  

def heaven(request):
    image = Image.objects.filter(image_location_id="2")
    context ={
        "post":image
    }
    return render(request,'all-images/first-images.html',context)  

def europe(request):
    image = Image.objects.filter(image_location_id="3")
    context ={
        "post":image
    }
    return render(request,'all-images/first-images.html',context)   

def mountains(request):
    image = Image.objects.filter(image_location_id="4")
    context ={
        "post":image
    }
    return render(request,'all-images/first-images.html',context)   

def africa(request):
    image = Image.objects.filter(image_location_id="5")
    context ={
        "post":image
    }
    return render(request,'all-images/first-images.html',context)     

def search_results(request):

    if 'post_image' in request.GET and request.GET["post_image"]:
        search_term = request.GET.get("post_image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'all-images/search.html',{"message":message,"postss":searched_images})
    else:
        message ="You haven't searched for anything"
        return render(request,'all-images/search.html',{'message':message})



 



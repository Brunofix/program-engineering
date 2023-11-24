from django.shortcuts import render
from django.http import HttpResponse
from .models import image

# Create your views here.
def homepage(request):
    count = image.objects.count()
    context = {
        "count": count,
    }
    return render(request, 'images/homepage.html', context) 


def image_list(request):
    images = image.objects.all()
    context = {
        "images": images,
    }
    return render(request,'images/image_list.html', context)

def image_detail(request, image_id):
    img = image.objects.get(id=image_id)
    context = {
        "image" : img,
    }
    return render(request, 'images/image_detail.html', context)
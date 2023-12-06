from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image
from django.http import HttpRequest
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def homepage(request):
    count = Image.objects.count()
    context = {
        "count": count,
    }
    return render(request,'images/homepage.html', context)

def image_list(request):
    images = Image.objects.all()
    context = {
        "images": images,
    }
    return render(request, 
                'images/image_list.html', 
                context)

def image_detail(request, image_id):
    image = Image.objects.get(id=image_id)
    comments = image.comment_set.all()
    is_liked = image.like_set.filter(user=request.user).first()
    context = {
        "image": image,
        "comments": comments,
        "is_liked": is_liked,
    }
    return render(request,
                  'images/image_detail.html',
                  context
                )

def create_image(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title", "")
        url = request.POST.get("url", "")
        pub_date=request.POST.get("pub_date", timezone.now())
        desc = request.POST.get("desc", "")
        image = Image(title=title, url=url, pub_date=pub_date, desc=desc)
        image.save()
        return HttpResponseRedirect(reverse("images:detail", args=(image.id,))) #mora ici zarez da ne misli da je image.id string

    context = {}
    return render(request, "images/create_image.html", context)

def create_comment(request, image_id):
    if request.user.is_authenticated:
        if request.method =="POST":
            image= get_object_or_404(Image, id=image_id)
            content = request.POST.get("content", "")
            image.comment_set.create(user=request.user, content=content)

    
    return HttpResponseRedirect(reverse("images:detail", args=(image_id,))) #mora ici zarez da ne misli da je image.id string


def toggle_like(request, image_id):
    if request.user.is_authenticated:
        image = get_object_or_404(Image, pk=image_id)
        like = image.like_set.filter(user=request.user).first()
        if like:
            like.delete()
        else:
            image.like_set.create(user=request.user)
    return HttpResponseRedirect(reverse("images:detail", args=(image_id,))) #mora ici zarez da ne misli da je image.id string
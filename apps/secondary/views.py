from django.shortcuts import render

# my imports
from apps.base.models import Settings
from .models import Pride,Gallery,Parlament
# Create your views here.

def pride_detail(request,id):
    setting = Settings.objects.latest("id")
    pride = Pride.objects.get(id =id)
    
    return render(request, "detail_pages/pride_detail.html",locals())

def gallery(request):
    setting = Settings.objects.latest("id")
    gallery = Gallery.objects.all()
    return render(request, "secondary/gallery.html",locals())

def gallery_detail(request,id):
    setting = Settings.objects.latest("id")
    gallery = Gallery.objects.get(id =id)
    return render(request, "detail_pages/gallery_detail.html",locals())

def parlament(request):
    setting = Settings.objects.latest("id")
    parlament = Parlament.objects.all()
    return render(request, "secondary/parlament.html",locals())
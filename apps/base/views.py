from django.shortcuts import render
# my imports
from apps.secondary.models import Slide,Pride,Data
from .models import Settings,About
# Create your views here.

def index(request):
    setting = Settings.objects.latest("id")
    slide = Slide.objects.latest("id")
    data = Data.objects.latest("id")
    pride = Pride.objects.all()
    return render(request, "base/index.html",locals())

def about(request):
    setting = Settings.objects.latest("id")
    about = About.objects.latest("id")
    data = Data.objects.latest("id")
    return render(request, "base/about.html",locals())
    
def contact(request):
    setting = Settings.objects.latest("id")
    return render(request, "base/contact.html",locals())
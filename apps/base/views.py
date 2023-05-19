from django.shortcuts import render
# my imports
from .models import Settings,About
# Create your views here.

def index(request):
    setting = Settings.objects.latest("id")
    return render(request, "base/index.html",locals())

def about(request):
    about = About.objects.latest("id")
    setting = Settings.objects.latest("id")
    return render(request, "base/about.html",locals())
    
def contact(request):
    setting = Settings.objects.latest("id")
    return render(request, "base/contact.html",locals())
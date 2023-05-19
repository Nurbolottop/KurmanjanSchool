from django.shortcuts import render
# my imports
from apps.secondary.models import Slide,Pride,Data,Certificate
from .models import Settings,About, New 
# Create your views here.

def index(request):
    setting = Settings.objects.latest("id")
    slide = Slide.objects.latest("id")
    data = Data.objects.latest("id")
    certificate = Certificate.objects.all()
    pride = Pride.objects.all()
    news = New.objects.all()
    return render(request, "base/index.html",locals())

def about(request):
    setting = Settings.objects.latest("id")
    about = About.objects.latest("id")
    data = Data.objects.latest("id")
    return render(request, "base/about.html",locals())
    
def contact(request):
    setting = Settings.objects.latest("id")
    return render(request, "base/contact.html",locals())

def news(request):
    setting = Settings.objects.latest("id")
    news = New.objects.all()
    return render(request, "base/news.html",locals())

def news_detail(request,id):
    setting = Settings.objects.latest("id")
    news = New.objects.get(id =id)
    return render(request, "detail_pages/news-details.html",locals())
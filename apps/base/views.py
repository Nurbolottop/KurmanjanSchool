from django.shortcuts import render,redirect
from django.core.mail import send_mail
# my imports
from apps.secondary.models import Slide,Pride,Data,Certificate
from .models import Settings,About, New, Teacher,Lessons,Contact
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
    lesson = Lessons.objects.all()
    
    return render(request, "base/about.html",locals())
    
def contact(request):
    setting = Settings.objects.latest("id")
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name = name,email = email,message = message)
        send_mail(
            f'{message}',
            f'Саламатсызбы {name}, билдируу калтырганыныз учун рахмат, Биз жакын арада байланышка чыгабыз.Сиздин билдируунуз: {message} Сиздин почтаныз: {email}',
            "noreply@somehost.local",
            [email])
        return redirect('index')
    return render(request, "base/contact.html",locals())

def news(request):
    setting = Settings.objects.latest("id")
    news = New.objects.all()
    return render(request, "base/news.html",locals())

def news_detail(request,id):
    setting = Settings.objects.latest("id")
    random_new = New.objects.all().order_by('?')
    news = New.objects.get(id =id)
    return render(request, "detail_pages/news-details.html",locals())

def teacher(request):
    setting = Settings.objects.latest("id")
    teacher = Teacher.objects.all()
    return render(request, "base/teacher.html",locals())
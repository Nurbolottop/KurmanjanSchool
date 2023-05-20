from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
        verbose_name="Сурот",
        blank = True, null = True
        )
    title = models.CharField(
        max_length=255,
        verbose_name="Слайдтын аты"
    )
    descriptions = models.TextField(
        verbose_name='Слайдка маалымат!'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайдтар"
        ordering = ('id', )
        
class Pride(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='pride/',
        verbose_name="Cурот",
        blank = True, null = True
        )
    name = models.CharField(
        max_length=255,
        verbose_name='Аты'
    )
    descriptions = models.TextField(
        verbose_name='Кошумча маалымат!'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сыймыктанган окуучубуз!"
        verbose_name_plural = "Сыймыктанган окуучуларыбыз!"
        ordering = ('id', )  

class Data(models.Model):
    years_school = models.CharField(
        max_length=255,
        verbose_name='Мугалимдердин саны'
    )
    child_school = models.CharField(
        max_length=255,
        verbose_name="Окуучулардын саны"
    )
    graduate_school = models.CharField(
        max_length=255,
        verbose_name='БҮТҮРҮҮЧҮЛӨР(ЖЫЛЫНА)'
    )
    book_school = models.CharField(
        max_length=255,
        verbose_name='КИТЕПТЕРДИН САНЫ'
    )

    def __str__(self):
        return self.years_school

    class Meta:
        verbose_name = 'Биз сандабыз!'
        verbose_name_plural = 'Биз сандабыз!'
        ordering = ('id', )

class Certificate(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='certificate/',
        verbose_name="Сурот",
        blank = True, null = True
        )

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = ' Сертификаттар'
        ordering = ('id', )
        
class Gallery(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Галерея '
        verbose_name_plural = 'Галерея'
        ordering = ('id', )


class GalleryDetail(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        on_delete= models.CASCADE,
        related_name="gallery",
        verbose_name="Галерея"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='gallery/',
        verbose_name="Сурот",
        blank = True, null = True
        )
    
    def __str__(self):
        return f"{str(self.gallery)}"
    
    class Meta:
        verbose_name = 'Галерея  болумго киргизуу'
        verbose_name_plural = 'Галерея  болумго киргизуу'
        ordering = ('id', )
        
class Lessons(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='Предметтин аты'
    )
    number = models.CharField(
        max_length=255,
        verbose_name="Сабак боюнча жетишкендиктер"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сабак'
        verbose_name_plural = ' Сабактар'
        ordering = ('id', )
        
class Parlament(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Окуучунун  аты.'
    )
    image  = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='parlament_image/',
        verbose_name="Окуучунун суроту",
        blank = True, null = True
    )
    descriptions = models.TextField(
        verbose_name='Окуучунун кызматы.'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Манас жаштар уюму"
        verbose_name_plural = "Манас жаштар уюму"
        ordering = ('id', )

class Student(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Класстын аты.'
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='students_image/',
        verbose_name="Окуучунун суроту",
        blank = True, null = True
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Класстар"
        verbose_name = "Класстар"
        ordering = ('id', )
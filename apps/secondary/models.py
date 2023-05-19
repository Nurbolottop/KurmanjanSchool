from django.db import models
from django_resized.forms import ResizedImageField

# Create your models here.
class Slide(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
        verbose_name="Фотография",
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
        verbose_name_plural = "Слайд"
        ordering = ('id', )
        
class Pride(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='slide/',
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
        verbose_name = "Сыймыктанабыз!"
        verbose_name_plural = "Сыймыктанабыз!"
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
        upload_to='slide/',
        verbose_name="Фотография",
        blank = True, null = True
        )

    class Meta:
        verbose_name = 'Сертификаттар'
        verbose_name_plural = 'Сертификат'
        ordering = ('id', )
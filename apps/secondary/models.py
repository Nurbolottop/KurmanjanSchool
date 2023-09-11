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
    child_school = models.CharField(
        max_length=255,
        verbose_name="Окуучулардын саны",
        blank=True,null=True,
    )
    class_comp = models.CharField(
        max_length=255,
        verbose_name="Класс комплекси",
        blank=True,null=True,
    )
    nol_class = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name="Башталгыч класс"
    )
    language = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name="Окутуу тили"
    )
    teacher_num = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name='Мугалимдердин саны'
    )
    great_teacher = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name='Жогорку билимдуу'
    )
    good_teacher = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name='Атайын орто билимдуу'
    )
    magister_teacher = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name="Магистр дипломуна ээ"
    )
    very_good_teacher = models.CharField(
        max_length=255,
        blank=True,null=True,
        verbose_name="Билим беруунун мыктысы"
    )
    
    def __str__(self):
        return self.child_school

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
        verbose_name = "Классты кошуу"
        verbose_name_plural = "Класстарды кошуу"
        ordering = ('id', )
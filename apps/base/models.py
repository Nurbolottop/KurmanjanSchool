from django.db import models
from django_resized.forms import ResizedImageField
# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Сайттын аты"
    )
    descriptions = models.TextField(
        verbose_name="Сайт боюнча маалымат"
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Телефон номер'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name='Youtube',
        blank=True, null=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Мектеп боюнча маалымат"
        verbose_name_plural = "Мектеп боюнча маалыматтар"
        ordering = ('id', )

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Биз жонундо кыскача маалымат"
    )
    descriptions = models.TextField(
        verbose_name="Биз жонундо кененрээк маалымат"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Биз жонундо сурот",
        blank = True,null = True    
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Биз жонундо"
        verbose_name_plural = "Биз жонундо"
        ordering = ('id', )

class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Сурот",
        blank = True,null = True    
    )
    descriptions = models.TextField(
        verbose_name="Кошумча маалымат"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанылык'
        verbose_name_plural = 'Жанылыктар'
        ordering = ('id', )

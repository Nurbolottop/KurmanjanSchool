from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Сайттын аты"
    )
    descriptions = models.TextField(
        verbose_name="Сайт боюнча маалымат"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Сайттын логотиби"
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
from django.db import models

# Create your models here.

class Parents(models.Model):
    name = models.CharField(
        max_length=244, 
        verbose_name='Документтин аты'
    )
    parents_doc = models.FileField(
        upload_to='parents_document/',
        verbose_name='Документ файл'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ата энелерге!"
        verbose_name_plural = "Ата эненлерге"
        ordering = ('id', )
     
class LessonsForPublic(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name='Аты'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ачык саатка сабак кошуу'
        verbose_name_plural = 'Ачык сааттарга сабак кошуу'
        ordering = ('id', )
   
class PublicLesson(models.Model):
    lessons = models.ForeignKey(
        LessonsForPublic,
        on_delete= models.CASCADE,
        related_name="lessons",
        verbose_name="Ачык саат"
    )
    file = models.FileField(
        upload_to='public_lesson/', 
        verbose_name='Документ файл'
    )
    title = models.CharField(
        max_length=255, 
        verbose_name='Аты'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ачык саат'
        verbose_name_plural = ' Ачык сааттар'
        ordering = ('id', )

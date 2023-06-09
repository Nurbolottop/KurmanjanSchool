# Generated by Django 4.2.1 on 2023-05-19 12:54

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slide',
            old_name='description_slide',
            new_name='descriptions',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='first_slide',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='second_slide',
        ),
        migrations.AddField(
            model_name='slide',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='slide/', verbose_name='Сурот'),
        ),
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Слайдтын аты'),
            preserve_default=False,
        ),
    ]

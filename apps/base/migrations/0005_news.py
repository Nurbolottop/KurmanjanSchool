# Generated by Django 4.2.1 on 2023-05-19 18:46

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_about_options_alter_settings_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='about_image', verbose_name='Сурот')),
            ],
        ),
    ]

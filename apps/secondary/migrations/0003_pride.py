# Generated by Django 4.2.1 on 2023-05-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0002_rename_description_slide_slide_descriptions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_pride/', verbose_name='Суроту!')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
                ('descriptions', models.TextField(verbose_name='Кошумча маалымат!')),
            ],
            options={
                'verbose_name': 'Сыймыктанабыз!',
                'verbose_name_plural': 'Сыймыктанабыз!',
                'ordering': ('id',),
            },
        ),
    ]

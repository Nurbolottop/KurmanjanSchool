# Generated by Django 4.2.1 on 2023-05-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LessonsForPublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Аты')),
            ],
            options={
                'verbose_name': 'Ачык саатка сабак кошуу',
                'verbose_name_plural': 'Ачык сааттарга сабак кошуу',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244, verbose_name='Документтин аты')),
                ('parents_doc', models.FileField(upload_to='parents_document/', verbose_name='Документ файл')),
            ],
            options={
                'verbose_name': 'Ата энелерге!',
                'verbose_name_plural': 'Ата эненлерге',
                'ordering': ('id',),
            },
        ),
    ]

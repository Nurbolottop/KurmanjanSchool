# Generated by Django 4.2.1 on 2023-05-19 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_about_alter_settings_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ('id',), 'verbose_name': 'Биз жонундо', 'verbose_name_plural': 'Биз жонундо'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'ordering': ('id',), 'verbose_name': 'Мектеп боюнча маалымат', 'verbose_name_plural': 'Мектеп боюнча маалыматтар'},
        ),
    ]
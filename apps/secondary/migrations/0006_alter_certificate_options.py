# Generated by Django 4.2.1 on 2023-05-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_certificate_alter_data_child_school_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ('id',), 'verbose_name': 'Сертификат', 'verbose_name_plural': ' Сертификаттар'},
        ),
    ]

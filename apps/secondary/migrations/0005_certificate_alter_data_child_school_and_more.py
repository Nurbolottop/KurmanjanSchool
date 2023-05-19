# Generated by Django 4.2.1 on 2023-05-19 17:59

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='slide/', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Сертификаттар',
                'verbose_name_plural': 'Сертификат',
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='data',
            name='child_school',
            field=models.CharField(max_length=255, verbose_name='Окуучулардын саны'),
        ),
        migrations.AlterField(
            model_name='data',
            name='graduate_school',
            field=models.CharField(max_length=255, verbose_name='БҮТҮРҮҮЧҮЛӨР(ЖЫЛЫНА)'),
        ),
        migrations.AlterField(
            model_name='data',
            name='years_school',
            field=models.CharField(max_length=255, verbose_name='Мугалимдердин саны'),
        ),
        migrations.AlterField(
            model_name='pride',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='slide/', verbose_name='Cурот'),
        ),
    ]

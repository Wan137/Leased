# Generated by Django 5.0.3 on 2024-03-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='flat / ')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('bedrooms', models.PositiveIntegerField(verbose_name='Спальня')),
                ('bathrooms', models.PositiveIntegerField(verbose_name='Ванная')),
                ('m2', models.PositiveIntegerField(verbose_name='Квадратные метры')),
                ('location', models.CharField(max_length=255, verbose_name='Местоположение')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Flat',
                'verbose_name_plural': 'Flats',
            },
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-25 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Flat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flats_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_flats', to='Flat.flats', verbose_name='Квартиры')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
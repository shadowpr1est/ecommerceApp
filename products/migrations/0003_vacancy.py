# Generated by Django 5.1.6 on 2025-03-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Имя и Фамилия')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('about', models.TextField(verbose_name='О себе')),
            ],
        ),
    ]

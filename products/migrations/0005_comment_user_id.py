# Generated by Django 5.1.6 on 2025-03-14 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-08-08 18:01

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_image', validators=[accounts.models.validate_image], verbose_name='프로필 이미지'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-07 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hoood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(default='About me', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='image.png', upload_to='profiles/'),
        ),
    ]
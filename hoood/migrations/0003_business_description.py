# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-07 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoood', '0002_remove_business_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='description',
            field=models.TextField(default='abc', max_length=200),
        ),
    ]

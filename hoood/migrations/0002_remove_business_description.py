# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-07 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoood', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='description',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 14:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0008_image_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
    ]

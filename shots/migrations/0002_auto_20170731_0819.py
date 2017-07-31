# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 08:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
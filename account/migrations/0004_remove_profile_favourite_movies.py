# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_favourite_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favourite_movies',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0003_auto_20170803_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(help_text='Your comment'),
        ),
        migrations.AlterField(
            model_name='image',
            name='body',
            field=models.TextField(blank=True, help_text="description(it's optional)"),
        ),
    ]
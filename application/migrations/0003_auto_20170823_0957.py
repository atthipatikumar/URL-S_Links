# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_urls_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='urls',
            name='shrinkedURL',
            field=models.CharField(max_length=8),
        ),
    ]

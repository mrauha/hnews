# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170905_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='vote',
            field=models.IntegerField(default=1),
        ),
    ]

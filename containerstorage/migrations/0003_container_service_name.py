# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-18 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containerstorage', '0002_auto_20160718_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='service_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
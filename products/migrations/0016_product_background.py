# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-12 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20200109_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='background',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='images'),
        ),
    ]

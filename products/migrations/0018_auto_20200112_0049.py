# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-12 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20200112_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='background',
            field=models.CharField(default='/media/images/background.jpg', editable=False, max_length=100),
        ),
    ]

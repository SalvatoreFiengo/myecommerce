# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-13 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_has_logged_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='reseller',
            field=models.BooleanField(),
        ),
    ]
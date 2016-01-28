# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20160112_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
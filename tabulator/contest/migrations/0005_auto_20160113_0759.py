# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_category_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterion',
            options={'verbose_name_plural': 'criteria'},
        ),
        migrations.RemoveField(
            model_name='criterion',
            name='sequence',
        ),
        migrations.AlterOrderWithRespectTo(
            name='criterion',
            order_with_respect_to='category',
        ),
    ]

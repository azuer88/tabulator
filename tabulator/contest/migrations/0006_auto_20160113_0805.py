# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20160113_0759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='criterion',
            options={'ordering': ['category', 'sequence'], 'verbose_name_plural': 'criteria'},
        ),
        migrations.AddField(
            model_name='criterion',
            name='sequence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterOrderWithRespectTo(
            name='criterion',
            order_with_respect_to=None,
        ),
    ]

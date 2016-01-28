# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0017_auto_20160120_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='dream',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='motto',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]

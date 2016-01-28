# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_auto_20160126_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='phase',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

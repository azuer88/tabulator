# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0013_auto_20160119_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

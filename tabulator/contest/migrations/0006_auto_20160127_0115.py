# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20160127_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]

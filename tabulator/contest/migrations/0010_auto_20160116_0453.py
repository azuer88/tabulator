# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_auto_20160116_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterion',
            name='short_name',
            field=models.CharField(max_length=30),
        ),
    ]

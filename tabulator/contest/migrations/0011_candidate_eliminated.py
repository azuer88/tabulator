# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0010_auto_20160116_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='eliminated',
            field=models.IntegerField(default=1),
        ),
    ]

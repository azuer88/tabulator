# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_auto_20160126_0614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='visible',
            new_name='is_visible',
        ),
    ]

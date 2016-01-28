# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_auto_20160127_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='active',
            new_name='is_active',
        ),
    ]

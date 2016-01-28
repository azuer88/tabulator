# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0011_candidate_eliminated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='eliminated',
            new_name='active',
        ),
    ]

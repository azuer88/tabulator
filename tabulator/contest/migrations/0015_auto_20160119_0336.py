# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_auto_20160119_0310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scorecriterion',
            options={'verbose_name_plural': 'Criteria Scores'},
        ),
    ]

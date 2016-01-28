# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0015_auto_20160119_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorecriterion',
            name='weighted_score',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
    ]

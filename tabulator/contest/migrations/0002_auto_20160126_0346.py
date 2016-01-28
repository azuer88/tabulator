# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_squashed_0019_scorecriterion_judge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecriterion',
            name='weighted_score',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
        migrations.AlterUniqueTogether(
            name='scorecriterion',
            unique_together=set([('candidate', 'criterion', 'judge')]),
        ),
    ]

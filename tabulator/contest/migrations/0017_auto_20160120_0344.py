# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0016_scorecriterion_weighted_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='age',
            field=models.PositiveIntegerField(default=19),
        ),
        migrations.AddField(
            model_name='candidate',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='candidate',
            name='nickname',
            field=models.CharField(default='', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='vital_statistics',
            field=models.CharField(default='', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

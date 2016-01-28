# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_auto_20160127_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='rankcategory',
            name='score',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0, 'Can not be lesser than 0'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100')]),
        ),
        migrations.AlterUniqueTogether(
            name='rankcategory',
            unique_together=set([('candidate', 'category', 'judge', 'rank')]),
        ),
    ]

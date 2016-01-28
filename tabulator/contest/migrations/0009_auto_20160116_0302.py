# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_auto_20160113_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Can not be lesser than 1%'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100%')]),
        ),
        migrations.AlterField(
            model_name='criterion',
            name='weight',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Can not be lesser than 1%'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100%')]),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0, 'Can not be lesser than 0'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0012_auto_20160119_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCriterion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0, 'Can not be lesser than 0'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100')])),
                ('candidate', models.ForeignKey(to='contest.Candidate')),
                ('criterion', models.ForeignKey(to='contest.Criterion')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='score',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='score',
            name='criterion',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
        migrations.AlterUniqueTogether(
            name='scorecriterion',
            unique_together=set([('candidate', 'criterion')]),
        ),
    ]

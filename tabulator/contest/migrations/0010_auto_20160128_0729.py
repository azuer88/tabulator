# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0009_auto_20160128_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoreCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, 'Can not be lesser than 0'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100')])),
                ('candidate', models.ForeignKey(to='contest.Candidate')),
                ('category', models.ForeignKey(to='contest.Category')),
                ('judge', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Category Scores',
            },
        ),
        migrations.RemoveField(
            model_name='rankcategory',
            name='score',
        ),
        migrations.AlterUniqueTogether(
            name='scorecategory',
            unique_together=set([('candidate', 'category', 'judge')]),
        ),
    ]

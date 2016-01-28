# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0007_auto_20160127_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rank', models.PositiveSmallIntegerField(default=1)),
                ('candidate', models.ForeignKey(to='contest.Candidate')),
                ('category', models.ForeignKey(to='contest.Category')),
                ('judge', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Category Ranking',
            },
        ),
        migrations.AlterUniqueTogether(
            name='rankcategory',
            unique_together=set([('candidate', 'category', 'judge')]),
        ),
    ]

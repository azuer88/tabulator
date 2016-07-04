# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0010_auto_20160128_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judge',
            name='user',
        ),
        migrations.AlterField(
            model_name='rankcategory',
            name='judge',
            field=models.ForeignKey(to='contest.Judge'),
        ),
        migrations.AlterField(
            model_name='scorecategory',
            name='judge',
            field=models.ForeignKey(to='contest.Judge'),
        ),
        migrations.AlterField(
            model_name='scorecriterion',
            name='judge',
            field=models.ForeignKey(to='contest.Judge'),
        ),
    ]

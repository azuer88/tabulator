# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0011_auto_20160215_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='user',
            field=models.OneToOneField(default=8, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rankcategory',
            name='judge',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scorecategory',
            name='judge',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scorecriterion',
            name='judge',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

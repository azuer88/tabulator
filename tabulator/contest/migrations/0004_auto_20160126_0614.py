# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_category_phase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['phase', 'sequence'], 'verbose_name_plural': 'Categories'},
        ),
    ]

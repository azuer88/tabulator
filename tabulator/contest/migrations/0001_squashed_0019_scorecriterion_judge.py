# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    replaces = [(b'contest', '0001_initial'), (b'contest', '0002_auto_20160112_0642'), (b'contest', '0003_candidate_gender'), (b'contest', '0004_category_visible'), (b'contest', '0005_auto_20160113_0759'), (b'contest', '0006_auto_20160113_0805'), (b'contest', '0007_auto_20160113_0809'), (b'contest', '0008_auto_20160113_0813'), (b'contest', '0009_auto_20160116_0302'), (b'contest', '0010_auto_20160116_0453'), (b'contest', '0011_candidate_eliminated'), (b'contest', '0012_auto_20160119_0110'), (b'contest', '0013_auto_20160119_0251'), (b'contest', '0014_auto_20160119_0310'), (b'contest', '0015_auto_20160119_0336'), (b'contest', '0016_scorecriterion_weighted_score'), (b'contest', '0017_auto_20160120_0344'), (b'contest', '0018_auto_20160120_0359'), (b'contest', '0019_scorecriterion_judge')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
                ('sequence', models.IntegerField()),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Can not be lesser than 1%'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100%')])),
            ],
            options={
                'ordering': ['sequence'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Criterion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(default='', max_length=200, blank=True)),
                ('sequence', models.IntegerField()),
                ('weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Can not be lesser than 1%'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100%')])),
                ('category', models.ForeignKey(to='contest.Category')),
            ],
            options={
                'ordering': ['category', 'sequence'],
                'verbose_name_plural': 'criteria',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField()),
                ('candidate', models.ForeignKey(to='contest.Candidate')),
                ('criterion', models.ForeignKey(to='contest.Criterion')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='group',
            field=models.ForeignKey(to='contest.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set([('candidate', 'criterion')]),
        ),
        migrations.AddField(
            model_name='candidate',
            name='gender',
            field=models.CharField(default='M', max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='visible',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterModelOptions(
            name='criterion',
            options={'verbose_name_plural': 'criteria'},
        ),
        migrations.RemoveField(
            model_name='criterion',
            name='sequence',
        ),
        migrations.AlterOrderWithRespectTo(
            name='criterion',
            order_with_respect_to='category',
        ),
        migrations.AlterModelOptions(
            name='criterion',
            options={'ordering': ['category', 'sequence'], 'verbose_name_plural': 'criteria'},
        ),
        migrations.AddField(
            model_name='criterion',
            name='sequence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterOrderWithRespectTo(
            name='criterion',
            order_with_respect_to=None,
        ),
        migrations.AlterModelOptions(
            name='criterion',
            options={'verbose_name_plural': 'criteria'},
        ),
        migrations.RemoveField(
            model_name='criterion',
            name='sequence',
        ),
        migrations.AlterOrderWithRespectTo(
            name='criterion',
            order_with_respect_to='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.IntegerField(verbose_name=(), validators=[django.core.validators.MinValueValidator(1, 'Can not be lesser than 1%'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100%')]),
        ),
        migrations.AlterField(
            model_name='criterion',
            name='weight',
            field=models.IntegerField(verbose_name=(), validators=[django.core.validators.MinValueValidator(1, 'Can not be lesser than 1%'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100%')]),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(verbose_name=(), validators=[django.core.validators.MinValueValidator(0, 'Can not be lesser than 0'), django.core.validators.MaxValueValidator(100, 'Can not be more than 100')]),
        ),
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
        migrations.AlterField(
            model_name='criterion',
            name='short_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AddField(
            model_name='candidate',
            name='active',
            field=models.IntegerField(default=1),
        ),
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
        migrations.AlterField(
            model_name='candidate',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterModelOptions(
            name='scorecriterion',
            options={'verbose_name_plural': 'Criteria Scores'},
        ),
        migrations.AddField(
            model_name='scorecriterion',
            name='weighted_score',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
            preserve_default=False,
        ),
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
        migrations.AddField(
            model_name='candidate',
            name='dream',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='motto',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='scorecriterion',
            name='judge',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

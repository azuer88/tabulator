"""
models.py
"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

def weight_field(*args, **kwargs):
    """
    retuns an IntegerField whose valid value is between 1 and 100
    """
    return models.IntegerField(args, kwargs, validators=[
        MinValueValidator(1, "Can not be lesser than 1%"),
        MaxValueValidator(100, "Can not be more than 100%")
    ])

def score_field(*args, **kwargs):
    """
    returns an IntegerField whose valid value is between 0 and 100
    """
    return models.IntegerField(args, kwargs, validators=[
        MinValueValidator(0, "Can not be lesser than 0"),
        MaxValueValidator(100, "Can not be more than 100")
    ])

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

# Create your models here.
class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u"{}".format(self.name)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().filter(visible__gt=0)

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    sequence = models.IntegerField()
    weight = weight_field()
    visible = models.IntegerField(default=1)

    objects = models.Manager()
    visibles = CategoryManager()

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['sequence']
        verbose_name_plural = 'Categories'


class Criterion(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = weight_field()

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        order_with_respect_to = 'category'
        verbose_name_plural = 'criteria'


class Group(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u"{}".format(self.name)


class Candidate(models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['number']


class Score(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    score = score_field()

    def __unicode__(self):
        return u"{}({}) = {}".format(
            self.candidate,
            self.criterion,
            self.score,
        )

    class Meta:
        unique_together = [('candidate', 'criterion'),]

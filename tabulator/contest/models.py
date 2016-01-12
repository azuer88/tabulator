from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

def weight_field():
    return models.IntegerField(validators=[
        MinValueValidator(1, "Can not be lesser than 1%"),
        MaxValueValidator(100, "Can not be more than 100%")
    ])


# Create your models here.
class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u"{}".format(self.name)

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    sequence = models.IntegerField()
    weight = weight_field()

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['sequence']


class Criterion(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200, blank=True, default='')
    sequence = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = weight_field()

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['category', 'sequence']


class Group(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u"{}".format(self.name)


class Candidate(models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['number']


class Score(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __unicode__(self):
        return u"{}".format(self.score)

    class Meta:
        unique_together = [('candidate','criterion'),]
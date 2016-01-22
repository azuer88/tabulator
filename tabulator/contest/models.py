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
    return models.IntegerField(*args, validators=[
        MinValueValidator(1, "Can not be lesser than 1%"),
        MaxValueValidator(100, "Can not be more than 100%")
    ], **kwargs)


def score_field(*args, **kwargs):
    """
    returns an IntegerField whose valid value is between 0 and 100
    """
    return models.IntegerField(*args, validators=[
        MinValueValidator(0, "Can not be lesser than 0"),
        MaxValueValidator(100, "Can not be more than 100")
    ], **kwargs)

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

def cm_to_feet_inches(cm):
    whole_inches = int(round(cm * 0.39370079))
    return (whole_inches / 12, whole_inches % 12)


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
    short_name = models.CharField(max_length=30)
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


class FemaleCandidate(models.Manager):
    def get_queryset(self):
        return super(FemaleCandidate, self).get_queryset() \
            .filter(gender='F', active=True)


class MaleCandidate(models.Manager):
    def get_queryset(self):
        return super(MaleCandidate, self).get_queryset() \
            .filter(gender='M', active=True)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30, default='', blank=True)
    age = models.PositiveIntegerField(default=19)
    vital_statistics = models.CharField(max_length=30, default='', blank=True)
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    number = models.PositiveIntegerField(default=0)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    motto = models.CharField(max_length=200, blank=True, default='')
    dream = models.CharField(max_length=200, blank=True, default='')

    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{}".format(self.name)

    objects = models.Manager()
    males = MaleCandidate()
    females = FemaleCandidate()

    class Meta:
        ordering = ['number']


class ScoreCriterion(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    score = score_field(default=100)
    weighted_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return u"{}({}) = {}".format(
            self.candidate,
            self.criterion,
            self.score,
        )

    class Meta:
        unique_together = [('candidate', 'criterion'), ]
        verbose_name_plural = 'Criteria Scores'
    # objects = models.Manager()


def get_candidate_scores(candidate, category):
    criteria = category.criterion_set.all()
    scores = []
    for criterion in criteria:
        score = ScoreCriterion.objects.get_or_create(candidate=candidate,
                                                     criterion=criterion)
        scores.append(score)
    return scores

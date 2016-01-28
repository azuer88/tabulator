"""
models.py
"""
from __future__ import unicode_literals

import decimal
from collections import defaultdict, OrderedDict
from itertools import groupby
from operator import itemgetter

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum, Avg  # , Value as V
# from django.db.models.functions import Concat


decimal.getcontext().prec = 2


def fk(*args, **kwargs):
    return models.ForeignKey(*args, on_delete=models.CASCADE, **kwargs)


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
    return whole_inches / 12, whole_inches % 12


# Create your models here.
class Judge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u"{}".format(self.name)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().filter(is_visible__gt=0)


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    sequence = models.IntegerField()
    weight = weight_field()
    is_visible = models.BooleanField(default=True)

    objects = models.Manager()
    visibles = CategoryManager()
    phase = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        ordering = ['phase', 'sequence']
        verbose_name_plural = 'Categories'


class Criterion(models.Model):
    short_name = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200, blank=True, default='')
    category = fk(Category)
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
            .filter(gender='F', is_active=True)


class MaleCandidate(models.Manager):
    def get_queryset(self):
        return super(MaleCandidate, self).get_queryset() \
            .filter(gender='M', is_active=True)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=30, default='', blank=True)
    age = models.PositiveIntegerField(default=19)
    vital_statistics = models.CharField(max_length=30, default='', blank=True)
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    number = models.PositiveIntegerField(default=0)
    group = fk(Group)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    motto = models.CharField(max_length=200, blank=True, default='')
    dream = models.CharField(max_length=200, blank=True, default='')

    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{}".format(self.name)

    def _get_height_english(self):
        feet, inches = cm_to_feet_inches(self.height)
        return u"{}' {}\"".format(feet, inches)

    english_height = property(_get_height_english)

    objects = models.Manager()
    males = MaleCandidate()
    females = FemaleCandidate()

    class Meta:
        ordering = ['number']


class ScoreCriterion(models.Model):
    candidate = fk(Candidate)
    criterion = fk(Criterion)
    judge = fk(User)
    score = score_field(default=100)
    weighted_score = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        # do something useful
        c_weight = self.criterion.weight / 100.00

        self.weighted_score = c_weight * self.score
        super(ScoreCriterion, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{}({}) = {}".format(
            self.candidate,
            self.criterion,
            self.score,
        )

    class Meta:
        unique_together = [('candidate', 'criterion', 'judge'), ]
        verbose_name_plural = 'Criteria Scores'
        # objects = models.Manager()


class RankCategory(models.Model):
    candidate = fk(Candidate)
    category = fk(Category)
    judge = fk(User)
    rank = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = [('candidate', 'category', 'judge', 'rank')]
        verbose_name_plural = 'Category Ranking'

    def __unicode__(self):
        return u"{}:{}({}) = {}".format(
            self.judge,
            self.candidate,
            self.category,
            self.rank,
        )


class ScoreCategory(models.Model):
    candidate = fk(Candidate)
    category = fk(Category)
    judge = fk(User)
    score = score_field(default=0)

    class Meta:
        unique_together = [('candidate', 'category', 'judge')]
        verbose_name_plural = 'Category Scores'

    def __unicode__(self):
        return u"{}:{}({}) = {}".format(
            self.judge,
            self.candidate,
            self.category,
        )


def populate_scores():
    _populate_scores(1, 100)
    _populate_scores(2, 0)


def _populate_scores(phase, score):
    import time
    start_time = time.time()
    # delete all previous scores
    ScoreCriterion.objects.filter(criterion__category__phase=phase).delete()

    candidates = Candidate.objects.all()
    categories = Category.visibles.filter(phase=phase)
    judges = User.objects.filter(is_active=True, is_staff=False)

    count = 0
    scores = []
    for candidate in candidates:
        for judge in judges:
            for category in categories:
                for criterion in category.criterion_set.all():
                    weight = criterion.weight
                    # ScoreCriterion.objects.create(
                    scores.append(
                        ScoreCriterion(
                            candidate=candidate,
                            criterion=criterion,
                            judge=judge,
                            score=score,
                            weighted_score=weight*score,
                        )
                    )
                    count += 1
    ScoreCriterion.objects.bulk_create(scores)
    duration = time.time() - start_time
    return count, duration


def rank_scores():
    RankCategory.objects.all().delete()
    _rank_scores('F')
    _rank_scores('M')


def consolidate_ranks():
    rank_scores()
    return {
        'female': _consolidate_ranks('F'),
        'male': _consolidate_ranks('M'),
    }


def _consolidate_ranks(gender, phase=1):
    qry = RankCategory.objects.filter(
        candidate__gender=gender,
        category__phase=phase) \
        .values('category__id', 'candidate__id') \
        .annotate(ave_rank=Avg('rank')) \
        .order_by('ave_rank') \
        .values_list('category__name', 'candidate__number', 'ave_rank')
    category_ids = Category.visibles.filter(phase=phase)\
                    .order_by('sequence')\
                    .values_list("name", flat=True)
    ranks = OrderedDict()
    for k in category_ids:
        ranks[k] = []
    for c_id, c_num, arank in qry:
        ranks[c_id].append({
            'number': c_num,
            'rank': arank,
        })
    return dict(ranks)

def _consolidate_scores(gender, phase=1):
    qry = ScoreCriterion.objects.filter(
        candidate__gender=gender,
        criterion__category__phase=phase)\
        .values('criterion__category', 'candidate', 'judge')\
        .annotate(wscore=Sum('weighted_score'))\
        .order_by("-wscore")\
        .values_list("candidate__id",
                     "criterion__category__id",
                     "criterion__category__weight",
                     "wscore",
                     "judge__id")

    scores = []
    for (candidate_id, category_id, weight, w_score, judge_id) in qry:
        scores.append({
            'category_id': category_id,
            'candidate_id': candidate_id,
            'judge_id': judge_id,
            'score': w_score * weight,
        })

    scores.sort(key=itemgetter('judge_id', 'candidate_id', 'category_id'))

    total_scores = defaultdict(list)
    for (jud_id, can_id), items in groupby(scores, key=itemgetter('judge_id', 'candidate_id')):
        total = decimal.Decimal(0.0)
        for elem in items:
            total += elem['score']
        total /= decimal.Decimal(100.00)

        total_scores[jud_id].append({
            'candidate_id': can_id,
            'score': total,
            'rank': 1,
        })


    for k in total_scores.keys():
        total_scores[k].sort(key=itemgetter('score'), reverse=True)

        for idx, member in enumerate(total_scores[k]):
            if idx == 0:
                continue
            prev_rank = total_scores[k][idx-1]['rank']
            prev_score = total_scores[k][idx-1]['score']
            cur_score = member['score']
            if cur_score < prev_score:
                member['rank'] = prev_rank + 1
            else:
                member['rank'] = prev_rank

    final_ranks = defaultdict(list)
    for k in total_scores.keys():
        for item in total_scores[k]:
            candidate_id = item['candidate_id']
            rank = item['rank']
            final_ranks[candidate_id].append(rank)

    final = []
    for k in final_ranks.keys():
        rank = decimal.Decimal(sum(final_ranks[k]))/decimal.Decimal(len(final_ranks[k]))
        final.append({
            'candidate_id': k,
            'rank': rank,
        })
    final.sort(key=itemgetter('rank'))

    return scores, total_scores, final


def _rank_scores(gender, phase=1):
    qry = ScoreCriterion.objects.filter(
        candidate__gender=gender,
        criterion__category__phase=phase)\
        .values('candidate', 'criterion__category', 'judge')\
        .annotate(wscore=Sum('weighted_score'))\
        .order_by("-wscore")\
        .values_list("candidate__id",
                     "criterion__category__id",
                     "wscore",
                     "judge__id")

    category_ids = Category.visibles.filter(phase=phase)\
                    .order_by('sequence')\
                    .values_list("id", flat=True)
    ranks = OrderedDict()
    for k in category_ids:
        ranks[k] = []

    # ranks = defaultdict(list)

    for (candidate_id, category_id, wscore, judge_id) in qry:
        rc = RankCategory()
        rc.candidate_id = candidate_id
        rc.category_id = category_id
        rc.judge_id = judge_id
        rc.score = wscore

        idx = len(ranks[category_id])
        if idx == 0:
            rc.rank = 1
        else:
            prev_rank = ranks[category_id][idx - 1].rank
            if ranks[category_id][idx - 1].score == rc.score:
                rc.rank = prev_rank
            else:
                rc.rank = prev_rank + 1.0

        ranks[category_id].append(rc)

    for k in ranks.keys():
        RankCategory.objects.bulk_create(ranks[k])
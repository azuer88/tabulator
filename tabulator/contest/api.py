from tastypie.resources import ModelResource
from tastypie import fields
from .models import Category, Criterion, Candidate, ScoreCriterion


class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'


class CriterionResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')

    class Meta:
        queryset = Criterion.objects.all()
        resource_name = 'criterion'


class CandidateResource(ModelResource):
    criterion = fields.ForeignKey(CriterionResource, 'criterion')

    class Meta:
        queryset = Candidate.objects.all()
        resource_name = 'candidate'


class ScoreResource(ModelResource):
    criterion = fields.ForeignKey(CriterionResource, 'criterion')
    candidate = fields.ForeignKey(CandidateResource, 'candidate')

    class Meta:
        queryset = ScoreCriterion.objects.all()
        resource_name = 'score'

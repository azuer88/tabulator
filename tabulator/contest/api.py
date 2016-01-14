from tastypie.resources import ModelResource
from .models import Category, Criterion, Candidate, Score


class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        
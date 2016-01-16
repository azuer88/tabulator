from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import Category, Criterion, Candidate, Score
from django.conf import settings

# Create your views here.
class ContestView(View):
    template_name = "base.html"

    def get(self, request):
        current_page = None
        category = Category.objects.first()
        criteria = category.criterion_set.all()
        candidates = Candidate.females.all()
        context = {
            'app_title': settings.APP_TITLE,
            'criteria': criteria,
            'category': category.name,
            'candidates': candidates,
        }
        return render(request, self.template_name, context=context)

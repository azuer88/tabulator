from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

from .models import Category, Criterion, Candidate, ScoreCriterion
from django.conf import settings

# Create your views here.
class ContestView(View):
    template_name = "angularjs.html"

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

def test_form(request):
    context = {
        'category': 'Production Number',
    }
    return render(request, "testform.html", context=context)

def get_candidate(request, candidate_id):
    # candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate = Candidate.objects.get(pk=candidate_id)
    context = {
        'candidate': candidate,
    }
    return render(request, "candidate.html", context=context)

@login_required
def index(request):
    #context = RequestContext(request)
    template_name = "bootstrap.html"
    category = Category.objects.first()
    criteria = category.criterion_set.all()

    male_ids = Candidate.males.order_by('number').values_list('id', 'number', flat=False)
    female_ids = Candidate.females.order_by('number').values_list('id', 'number', flat=False)

    context = {
            'app_title': settings.APP_TITLE,
            'criteria': criteria,
            'category': category.name,
            'males': male_ids,
            'females': female_ids,
    }

    return render(request, template_name, context=context)

def logout_view(request):
    logout(request)
    return redirect(reverse('contest-login'))
from operator import itemgetter
from itertools import groupby

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from django.views.generic import View
from django.contrib.auth import logout, authenticate, login
from django.core.urlresolvers import reverse

from .models import Category, Criterion, Candidate, ScoreCriterion
from .models import consolidate_ranks, consolidate_scores

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

@login_required
def get_candidate(request, candidate_id, phase):
    from django.contrib.auth.models import User
    # candidate = get_object_or_404(Candidate, pk=candidate_id)
    candidate = Candidate.objects.get(pk=candidate_id)
    categories = Category.visibles.filter(phase=phase).order_by('sequence')

    scores = ScoreCriterion.objects.filter(
        candidate=candidate,
        # judge=request.user,
        judge=User.objects.get(username='judge1'),
        criterion__category__is_visible=True,
        criterion__category__phase=phase,
    ).order_by('candidate', 'judge', 'criterion__category__sequence') \
      .values('criterion__category__id', 'criterion__category__name', 'criterion__id', 'criterion__name', 'score')
    data = []
    for category, items in groupby(scores, key=itemgetter('criterion__category__name')):
       cat_id = None
       m = []
       for item in items:
           if cat_id is None:
               cat_id = item['criterion__category__id']
           m.append({
               'criterion_id': item['criterion__id'],
               'criterion': item['criterion__name'],
               'score': item['score'],
           })
       rec = {
           'category': category,
           'category_id': cat_id,
           'items': m,
       }
       data.append(rec)

    context = {
        'candidate': candidate,
        'judge_id': request.user.id,
        'data': data,
    }
    return render(request, "candidate.html", context=context)

@login_required
def index(request):
    #context = RequestContext(request)
    template_name = "elimination.html"
    category = Category.objects.first()
    criteria = category.criterion_set.all()


    male_ids = Candidate.males.order_by('number').values_list('id', 'number', flat=False)
    female_ids = Candidate.females.order_by('number').values_list('id', 'number', flat=False)
    first = female_ids[0][0]

    context = {
            'app_title': settings.APP_TITLE,
            'criteria': criteria,
            'category': category.name,
            'males': male_ids,
            'females': female_ids,
            'first': first,
    }

    return render(request, template_name, context=context)


@login_required
def final_view(request):
    #context = RequestContext(request)
    template_name = "finals.html"
    category = Category.objects.first()
    criteria = category.criterion_set.all()


    male_ids = Candidate.males.order_by('number').values_list('id', 'number', flat=False)
    female_ids = Candidate.females.order_by('number').values_list('id', 'number', flat=False)
    first = female_ids[0][0]

    context = {
            'app_title': settings.APP_TITLE,
            'criteria': criteria,
            'category': category.name,
            'males': male_ids,
            'females': female_ids,
            'first': first,
    }

    return render(request, template_name, context=context)


def logout_view(request):
    logout(request)
    return redirect(reverse('contest-login'))

def login_view(request):
    logout(request)
    if request.POST:
        username = request.POST['user']
        password = request.POST['pass']
        next = request.POST.get('next', None)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(next)
    else:
        next = request.GET.get('next', None)
        if next is None:
            next = '/contest/'

    context = {
        'next': next,
    }

    return render(request, 'login.html', context=context)

@login_required
def set_score(request):
    name_str = request.GET['name']
    value_str = request.GET['value']

    candidate_id, criterion_id, judge_id = name_str.split('.')
    score, dummy = ScoreCriterion.objects.get_or_create(
        candidate__id=candidate_id,
        criterion__id=criterion_id,
        judge__id=judge_id,
    )
    score.score = int(value_str)
    score.save()
    result = {}
    result['code'] = 200
    result['message'] = "Got {} = {}".format(name_str, value_str)
    return JsonResponse(result)

@login_required
def get_score(request):
    result = {}
    result['code'] = 200
    result['message'] = 'OK'
    return JsonResponse(result)

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def minor_awards(request):
    m = consolidate_ranks()
    colw = 12 / len(m['female'].keys())
    context = {
        'ranks': m,
        'colw': colw,
    }
    return render(request, 'ranks.html', context=context)

@staff_member_required
def rank_candidates(request):
    m = consolidate_scores()
    context = {
        'ranks': m,
        'title': 'List of Finalists'
    }
    return render(request, 'ranks_overall.html', context=context)

@staff_member_required
def rank_finalists(request):
    m = consolidate_scores(phase=2)
    context = {
        'ranks': m,
        'title': 'List of Winners'
    }
    return render(request, 'ranks_overall.html', context=context)
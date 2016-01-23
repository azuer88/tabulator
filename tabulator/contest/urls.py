from django.conf.urls import url
from views import ContestView, index, test_form, get_candidate

urlpatterns = [
    url(r'^$', index, name='contest-index'),
    url(r'testform/', test_form, name='get-test-form'),
    url(r'candidate/(?P<candidate_id>[0-9])/$', get_candidate, name='get-candidate'),
    url(r'login/$', 'django.contrib.auth.views.login', name='contest-login'),
    url(r'logout/$', 'contest.views.logout', name='contest-logout'),
    #url(r'', ContestView.as_view()),
]

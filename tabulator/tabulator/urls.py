"""tabulator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponseRedirect

# serve static files during development
from django.conf import settings
from django.conf.urls.static import static
from tastypie.api import Api

from contest.api import CategoryResource, CriterionResource
from contest.api import CandidateResource, ScoreResource

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns.append(
    url(r'^contest/', include('contest.urls')),
)

# redirect to contest if url is blank
urlpatterns.append(
    url(r'^$', lambda r: HttpResponseRedirect('contest/')),
)

# add resources' urls
api = Api(api_name='v1')
api.register(CategoryResource())
api.register(CriterionResource())
api.register(CandidateResource())
api.register(ScoreResource())
# catres = CategoryResource()
urlpatterns.append(
    url(r'^api/', include(api.urls))
)

# serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

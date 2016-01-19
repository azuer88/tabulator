from django.conf.urls import url
from views import ContestView, index

urlpatterns = [
    url(r'test/', index, name='test'),
    url(r'', ContestView.as_view()),
]

from django.conf.urls import url
from views import ContestView

urlpatterns = [
    url(r'', ContestView.as_view()),
]

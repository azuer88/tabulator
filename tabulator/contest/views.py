from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class ContestView(View):
    template_name = "index.html"
    def get(self, request):
        return render(request, self.template_name)


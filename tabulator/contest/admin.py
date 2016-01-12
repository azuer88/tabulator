from django.contrib import admin

from models import Category, Criterion, Group, Candidate, Score

# Register your models here.
admin.site.register(Candidate)
admin.site.register(Criterion)
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Score)

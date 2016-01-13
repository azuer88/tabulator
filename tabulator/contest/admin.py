from django.contrib import admin

from models import Category, Criterion, Group, Candidate, Score

# Register your models here.
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'group')

admin.site.register(Criterion)
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(Score)

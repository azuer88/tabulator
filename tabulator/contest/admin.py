from django.contrib import admin

from models import Category, Criterion, Group, Candidate, ScoreCriterion

# Register your models here.


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'group')


class CriteriaInline(admin.TabularInline):
    model = Criterion


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CriteriaInline,
    ]


# admin.site.register(Criterion)
# admin.site.register(Category)

admin.site.register(Group)
admin.site.register(ScoreCriterion)

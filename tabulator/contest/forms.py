from django.forms import ModelForm
from .models import Score

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ['candidate', 'criterion', 'score']

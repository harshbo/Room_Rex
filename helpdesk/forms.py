from django.forms import ModelForm
from .models import Problem

class ProblemForm(ModelForm):
  class Meta:
    model=Problem
    fields ="__all__"
    
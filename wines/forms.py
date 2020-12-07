from django import forms
from .models import Wine

# Made a comment here
class WineForm(forms.ModelForm):
  class Meta:
    model = Wine
    fields = ['wine_name', 'price', 'varietal', 'description']

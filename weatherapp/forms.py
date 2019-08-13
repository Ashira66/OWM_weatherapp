from django import forms
from .models import weatherdata

class LocationForm(forms.ModelForm):

class Meta:
    model = weatherdata
    fields = ('Location')

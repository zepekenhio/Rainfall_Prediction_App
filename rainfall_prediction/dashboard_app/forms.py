from dataclasses import fields
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['pressure', 'max_temp', 'temp',  'min_temp',  'dewpoint', 'humidity', 'cloud', 'sunshine', 'wind_direction', 'wind_speed']
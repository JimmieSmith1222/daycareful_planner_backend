from django import forms
from .models import ParentInfo

class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = ['name', 'kidsName', 'paid', 'attendance']

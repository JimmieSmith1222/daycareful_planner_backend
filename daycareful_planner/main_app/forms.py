from django import forms
from .models import ParentInfo, ChildInfo

class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = ['name', 'kidsName', 'paid', 'attendance']
        
class ChildForm(forms.ModelForm):
    class Meta:
        model = ChildInfo
        fields = ['name', 'age', 'allergies']


from django import forms
from .models import ParentInfo, ChildInfo, EmployeeInfo

class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = ['name', 'kidsName', 'paid', 'attendance', 'image']
        
class ChildForm(forms.ModelForm):
    class Meta:
        model = ChildInfo
        fields = ['name', 'age', 'allergies', 'image']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeInfo
        fields = ['name', 'hours', 'attendance', 'pay', 'position', 'image']

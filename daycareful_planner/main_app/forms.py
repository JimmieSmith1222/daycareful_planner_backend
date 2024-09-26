from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ParentInfo, ChildInfo, EmployeeInfo

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentInfo
        fields = ['name', 'kidsName', 'paid', 'attendance', 'image']
        
    def save(self, commit=True, *args, **kwargs):
        obj = super(ParentForm, self).save(commit=False, *args, **kwargs)
        if commit:
            obj.user = kwargs.get('user', None)
            obj.save()
        return obj
        
class ChildForm(forms.ModelForm):
    class Meta:
        model = ChildInfo
        fields = ['name', 'age', 'allergies', 'image']
    
    def save(self, commit=True, *args, **kwargs):
        obj = super(ChildForm, self).save(commit=False, *args, **kwargs)
        if commit:
            obj.user = kwargs.get('user', None)
            obj.save()
        return obj

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeInfo
        fields = ['name', 'hours', 'attendance', 'pay', 'position', 'image']
        
    def save(self, commit=True, *args, **kwargs):
        obj = super(EmployeeForm, self).save(commit=False, *args, **kwargs)
        if commit:
            obj.user = kwargs.get('user', None)
            obj.save()
        return obj

from django.shortcuts import render
from .models import ParentInfo, ChildInfo, EmployeeInfo

def index(request):
    parents = ParentInfo.objects.all()
    children = ChildInfo.objects.all()
    employees = EmployeeInfo.objects.all()
    return render(request, 'index.html', {
        'parents': parents,
        'children': children,
        'employees': employees
    })
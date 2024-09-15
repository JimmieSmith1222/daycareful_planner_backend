from django.shortcuts import render, get_object_or_404, redirect
from .models import ParentInfo, ChildInfo, EmployeeInfo
from .forms import ParentForm, ChildForm, EmployeeForm

def home(request):
    return render(request, 'home.html')

def parent_list(request):
    parents = ParentInfo.objects.all()
    return render(request, 'parent/parent_list.html', {'parents': parents})

def parent_detail(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    return render(request, 'parent/parent_detail.html', {'parent': parent})

def parent_create(request):
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            parent = form.save()
            return redirect('parent_list')
    else:
        form = ParentForm()
    return render(request, 'parent/parent_form.html', {'form': form})

def parent_edit(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    if request.method == "POST":
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            parent = form.save()
            return redirect('parent_detail', id=parent.id)
    else:
        form = ParentForm(instance=parent)
    return render(request, 'parent/parent_form.html', {'form': form})

def parent_delete(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    if request.method == "POST":
        parent.delete()
        return redirect('parent_list')
    return render(request, 'parent/parent_confirm_delete.html', {'parent': parent})

def child_list(request):
    children = ChildInfo.objects.all()
    return render(request, 'child/child_list.html', {'children': children})

def child_detail(request, id):
    child = get_object_or_404(ChildInfo, id=id)
    return render(request, 'child/child_detail.html', {'child': child})

def child_create(request):
    if request.method == "POST":
        form = ChildForm(request.POST)
        if form.is_valid():
            child = form.save()
            return redirect('child_list')
    else:
        form = ChildForm()
    return render(request, 'child/child_form.html', {'form': form})

def child_edit(request, id):
    child = get_object_or_404(ChildInfo, id=id)
    if request.method == "POST":
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            child = form.save()
            return redirect('child_detail', id=child.id)
    else:
        form = ChildForm(instance=child)
    return render(request, 'child/child_form.html', {'form': form})

def child_delete(request, id):
    child = get_object_or_404(ChildInfo, id=id)
    if request.method == "POST":
        child.delete()
        return redirect('child_list')
    return render(request, 'child/child_confirm_delete.html', {'child': child})

def employee_list(request):
    employees = EmployeeInfo.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

def employee_detail(request, id):
    employee = get_object_or_404(EmployeeInfo, id=id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_edit(request, id):
    employee = get_object_or_404(EmployeeInfo, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('employee_detail', id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_delete(request, id):
    employee = get_object_or_404(EmployeeInfo, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})

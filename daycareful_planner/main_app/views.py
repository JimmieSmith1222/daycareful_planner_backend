from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import ParentInfo, ChildInfo, EmployeeInfo
from .forms import ParentForm, ChildForm, EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def parent_list(request):
    parents = ParentInfo.objects.filter(user=request.user)
    return render(request, 'parent/parent_list.html', {'parents': parents})

@login_required
def parent_detail(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    return render(request, 'parent/parent_detail.html', {'parent': parent})

@login_required
def parent_create(request):
    if request.method == "POST":
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            parent_info = form.save(commit=False)
            parent_info.user = request.user
            parent_info.save()
            return redirect('parent_list')
    else:
        form = ParentForm()
    return render(request, 'parent/parent_form.html', {'form': form})

@login_required
def parent_edit(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    if request.method == "POST":
        form = ParentForm(request.POST, request.FILES, instance=parent)
        if form.is_valid():
            if 'delete_image' in request.POST and request.POST['delete_image'] == 'on':
                parent.image.delete()
                parent.image = None
            parent_info = form.save(commit=False)
            parent_info.user = parent.user
            parent_info.save()
            return redirect('parent_detail', id=parent.id)
    else:
        form = ParentForm(instance=parent)
    return render(request, 'parent/parent_form.html', {'form': form})

@login_required
def parent_delete(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    if request.method == "POST":
        parent.delete()
        return redirect('parent_list')
    return render(request, 'parent/parent_confirm_delete.html', {'parent': parent})

@login_required
def delete_parent_image(request, id):
    parent = get_object_or_404(ParentInfo, id=id)
    if request.method == 'POST':
        parent.image.delete()
        parent.image = None
        parent.save()
        return redirect('parent_detail', id=id)
    return render(request, 'parent/confirm_delete_image.html', {'parent': parent})

@login_required
def child_list(request):
    children = ChildInfo.objects.filter(user=request.user)
    return render(request, 'child/child_list.html', {'children': children})

@login_required
def child_detail(request, id):
    child = get_object_or_404(ChildInfo, id=id)
    return render(request, 'child/child_detail.html', {'child': child})

@login_required
def child_create(request):
    if request.method == "POST":
        form = ChildForm(request.POST, request.FILES)
        if form.is_valid():
            child_info = form.save(commit=False)
            child_info.user = request.user
            child_info.save()
            return redirect('child_list')
    else:
        form = ChildForm()
    return render(request, 'child/child_form.html', {'form': form})

@login_required
def child_edit(request, id):
    child = get_object_or_404(ChildInfo, id=id)
    if request.method == "POST":
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            child_info = form.save(commit=False)
            child_info.user = child.user
            child_info.save()
            return redirect('child_detail', id=child.id)
    else:
        form = ChildForm(instance=child)
    return render(request, 'child/child_form.html', {'form': form})

@login_required
def child_delete(request, id):
    child = get_object_or_404(ChildInfo, id=id)
    if request.method == "POST":
        child.delete()
        return redirect('child_list')
    return render(request, 'child/child_confirm_delete.html', {'child': child})

@login_required
def employee_list(request):
    employees = EmployeeInfo.objects.filter(user=request.user)
    return render(request, 'employee/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, id):
    employee = get_object_or_404(EmployeeInfo, id=id)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

@login_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee_info = form.save(commit=False)
            employee_info.user = request.user
            employee_info.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def employee_edit(request, id):
    employee = get_object_or_404(EmployeeInfo, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee_info = form.save(commit=False)
            employee_info.user = employee.user
            employee_info.save()
            return redirect('employee_detail', id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def employee_delete(request, id):
    employee = get_object_or_404(EmployeeInfo, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})

def custom_logout(request):
    print("Logout view triggered")
    logout(request)
    return redirect('/')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
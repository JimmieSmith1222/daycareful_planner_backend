from django.shortcuts import render, get_object_or_404, redirect
from .models import ParentInfo
from .forms import ParentForm

#def index(request):
#    parents = ParentInfo.objects.all()
#    children = ChildInfo.objects.all()
#    employees = EmployeeInfo.objects.all()
#    return render(request, 'index.html', {
#        'parents': parents,
#        'children': children,
#        'employees': employees
#    })

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
            return redirect('parent_detail', id=parent.id)
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



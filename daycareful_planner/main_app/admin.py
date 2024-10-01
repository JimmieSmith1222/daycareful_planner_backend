from django.contrib import admin
from .models import ParentInfo, ChildInfo, EmployeeInfo

admin.site.register(ParentInfo)
admin.site.register(ChildInfo)
admin.site.register(EmployeeInfo)
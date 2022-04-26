from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','company_name','Employee_members','user']
    list_editable = ['company_name','Employee_members']
    list_per_page = 100
    list_select_related = ['user']

@admin.register(models.Job)
class JobModel(admin.ModelAdmin):
    list_display = ['id','title','description','Employee']
    list_editable = ['title','description']
    list_per_page = 100
    list_select_related = ['Employee']


from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Applied_Job)
class AppliedModel(admin.ModelAdmin):
    list_display = ['id','job','candidate']
    list_per_page = 100
    list_select_related = ['job','candidate']

from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Candidate)
class CandidateModel(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','gender','career','detail','national_id']
    list_editable = ['career','detail','national_id']
    list_per_page = 100
    list_select_related = ['user']

@admin.register(models.WorkExperience)
class WorkExperienceModel(admin.ModelAdmin):
    list_display = ['id','title','company_name','start_date','end_date','Candidate']
    list_editable = ['title','company_name']
    list_per_page = 100
    list_select_related = ['Candidate']

@admin.register(models.Skill)
class SkillModel(admin.ModelAdmin):
    list_display = ['id','skill','level','Candidate']
    list_editable = ['skill','level',]
    list_per_page = 100
    list_select_related = ['Candidate']

@admin.register(models.Language)
class LanguageModel(admin.ModelAdmin):
    list_display = ['id','language','level','Candidate']
    list_editable = ['language','level']
    list_per_page = 100
    list_select_related = ['Candidate']

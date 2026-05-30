from django.contrib import admin
from .models import Project, Lead

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'category', 'capacity_kw')
    list_filter = ('category', 'location')

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location', 'project_scale', 'submitted_at')
    readonly_fields = ('submitted_at',)
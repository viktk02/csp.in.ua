from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Project

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title',)
    ordering = ('-date_posted',)
    date_hierarchy = 'date_posted'
    fields = ('title', 'content', 'date_posted', 'image')
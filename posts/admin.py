from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'date_posted', 'preview_text')
    list_filter = ('date_posted',)
    search_fields = ('title',)
    ordering = ('-date_posted',)
    date_hierarchy = 'date_posted'
    fields = ('title', 'preview_text', 'content', 'date_posted', 'image',)


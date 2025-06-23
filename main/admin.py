from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import CarouselImage, PartnerLogo, AboutUs, MainPage


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }

class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsForm

    def has_add_permission(self, request):
        return not AboutUs.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = '__all__'
        widgets = {
            'content': CKEditor5Widget(config_name='default'),
        }

class MainPageAdmin(admin.ModelAdmin):
    form = MainPageForm

    def has_add_permission(self, request):
        return not AboutUs.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(CarouselImage)
admin.site.register(PartnerLogo)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(MainPage, MainPageAdmin)
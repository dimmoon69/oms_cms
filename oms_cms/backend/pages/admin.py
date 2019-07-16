from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.contenttypes.admin import GenericStackedInline

from oms_cms.backend.oms_seo.models import Seo
from oms_cms.backend.news.admin import ActionPublish

from .models import Pages


class PagesAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Pages
        fields = '__all__'


class SeoInlines(GenericStackedInline):
    """Seo"""
    model = Seo
    # extra = 1
    max_num = 1


@admin.register(Pages)
class PagesAdmin(ActionPublish):
    """Статичные страницы"""
    list_display = ("title", "lang", "published", "id")
    list_editable = ("published", )
    list_filter = ("published", "lang", "template")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title", )}
    form = PagesAdminForm
    actions = ['unpublish', 'publish']
    inlines = [SeoInlines]





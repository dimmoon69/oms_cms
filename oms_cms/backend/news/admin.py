from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from oms_cms.backend.oms_seo.admin import SeoInlines
#from oms_cms.backend.comments.admin import CommentsInlines
from oms_cms.backend.utils.admin import ActionPublish

from .models import Post, Category, Tags


class PostAdminForm(forms.ModelForm):
    """Виджет редактора ckeditor"""
    mini_text = forms.CharField(label="Превью статьи", widget=CKEditorUploadingWidget())
    text = forms.CharField(label="Полная статья", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin, ActionPublish):
    """Категории"""
    list_display = ("name", "slug", "published", "sort", "id")
    list_display_links = ("name",)
    list_filter = ("name", "published")
    list_editable = ("published", "sort")
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 20
    actions = ['unpublish', 'publish']
    inlines = (SeoInlines,)


@admin.register(Tags)
class TagsAdmin(ActionPublish):
    """Категории"""
    list_display = ("name", "published")
    list_filter = ("published",)
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("name",)}
    actions = ['unpublish', 'publish']
    search_fields = ("name", )


@admin.register(Post)
class PostAdmin(ActionPublish):
    """Статьи"""
    form = PostAdminForm
    list_display = ('title', 'lang', 'created_date', 'category', 'published', "sort", 'id')
    list_filter = ('lang', 'created_date', 'category', 'published')
    list_editable = ("published", "sort")
    search_fields = ["title", "category", "tag"]
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']
    save_as = True
    autocomplete_fields = ["tag"]
    readonly_fields = ('viewed',)

    inlines = (SeoInlines,)# CommentsInlines,)

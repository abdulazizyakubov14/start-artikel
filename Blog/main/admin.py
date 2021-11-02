from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
# Register your models here.

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):
    list_display = ['title', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}